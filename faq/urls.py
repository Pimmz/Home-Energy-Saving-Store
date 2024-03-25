from django.urls import path
from .views import FAQView

urlpatterns = [
    path('faq/', FAQView.as_view(), name='faq'),
]
