from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('', include('contact.urls')),
    path('', include('tips_and_tricks.urls')),
    path('', include('faq.urls')),
    path('400/', views.custom_400.as_view(), name='custom_400'),
    path('403/', views.custom_403.as_view(), name='custom_403'),
    path('404/', views.custom_404.as_view(), name='custom_404'),
    path('500/', views.custom_500.as_view(), name='custom_500'),
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

