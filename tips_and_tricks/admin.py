from django.contrib import admin
from .models import TipsAndTricks, ApprovalStatus

class ApprovalStatusAdmin(admin.ModelAdmin):
    list_display = ['post','is_approved']
    actions = ['approve_posts']

    def approve_posts(self, request, queryset):
        for approval_status in queryset:
            approval_status.is_approved = True
            approval_status.post.is_approved = True
            approval_status.post.save()
            approval_status.save()

        self.message_user(request, "Selected posts have been approved.")

admin.site.register(TipsAndTricks)
admin.site.register(ApprovalStatus, ApprovalStatusAdmin)
