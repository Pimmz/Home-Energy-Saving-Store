from django.urls import path
from .views import CustomBadRequestView, CustomPageNotFoundView, CustomPermissionDeniedView, CustomServerErrorView

urlpatterns = [
    path('400/', CustomBadRequestView.as_view(), name='bad_request'),
    path('403/', CustomPermissionDeniedView.as_view(), name='permission_denied'),
    path('404/', CustomPageNotFoundView.as_view(), name='page_not_found'),
    path('500/', CustomServerErrorView.as_view(), name='server_error'),   
]
