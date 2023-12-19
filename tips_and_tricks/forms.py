from django import forms
from .models import TipsAndTricks


class PostForm(forms.ModelForm):
    class Meta:
        model = TipsAndTricks
        fields = ['title', 'content', 'featured_image']
     