from django.urls import path
from .views import TipsAndTricksView, AddPostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('tips_and_tricks/', TipsAndTricksView.as_view(), name='tips_and_tricks'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('update_post/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('delete_post/<int:pk>', DeletePostView.as_view(), name='delete_post'),
]
