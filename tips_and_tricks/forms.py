from django import forms
from .models import TipsAndTricks


class PostCreateForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3 })
    )
    class Meta:
        model = TipsAndTricks
        fields = ['title', 'content', 'featured_image']
     