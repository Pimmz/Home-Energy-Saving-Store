from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect
from .models import TipsAndTricks
from .forms import PostForm


class TipsAndTricksView(View):
    def get(self, request):
        posts = TipsAndTricks.objects.filter(is_approved=True)
        return render(request, 'tips_and_tricks.html', {'posts': posts})

    def post(self, request):
        if not request.user.is_authenticated:
            messages.error(request, 'You must be logged in to add a post.')
            return redirect('login')

        form = PostForm(request.POST)     
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post added successfully. Waiting for Approval.')
            return redirect('tips_and_tricks')      
        else:
            messages.error(request, 'Error adding post. Please check the form.')

        return render(request, 'add_post.html', {'form': form})
