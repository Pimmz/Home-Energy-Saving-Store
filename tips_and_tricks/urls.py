from django.urls import path
from .views import TipsAndTricksView

urlpatterns = [
    path('tips_and_tricks/', TipsAndTricksView.as_view(), name='tips_and_tricks'),
]
