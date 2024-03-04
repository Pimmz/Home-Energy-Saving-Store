from django.urls import path
from .views import TipsAndTricksView, AddPostView

urlpatterns = [
    path('tips_and_tricks/', TipsAndTricksView.as_view(), name='tips_and_tricks'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
]
