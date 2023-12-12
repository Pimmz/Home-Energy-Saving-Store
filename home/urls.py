from django.urls import path
from .views import BadRequestView, PermissionDeniedView, PageNotFoundView, ServerErrorView
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('400/', BadRequestView.as_view(), name='bad_request'),
    path('403/', PermissionDeniedView.as_view(), name='permission_denied'),
    path('404/', PageNotFoundView.as_view(), name='page_not_found'),
    path('500/', ServerErrorView.as_view(), name='server_error'),
    
]
