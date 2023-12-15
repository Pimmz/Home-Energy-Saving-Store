from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect
from .models import TipsAndTricks
from .forms import PostCreateForm


class TipsAndTricksView(View):
    def get(self, request, *args, **kwargs):
        form = PostCreateForm()
        return render(request, 'tips.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = PostCreateForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Your Post has been successful')
            return redirect('tips_and_tricks')
        else:
            messages.error(request, 'There was an error with your post')
            return render(request, 'tips.html', {'form': form})
