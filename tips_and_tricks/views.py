from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect
from .models import TipsAndTricks
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator


class TipsAndTricksView(View):
    def get(self, request):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                posts = TipsAndTricks.objects.all()
            else:
                posts = TipsAndTricks.objects.filter(is_approved=True)

            paginator = Paginator(posts, 6)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            return render(request, 'tips_and_tricks.html', {'page_obj': page_obj})
        else:
            messages.error(request, 'You must be logged in to view this page.')
            return redirect('login')

class AddPostView(LoginRequiredMixin, View):
    def get(self, request):
        form = PostForm()
        return render(request, 'add_post.html', {'form':form})

    def post (self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post added successfully. Waiting for Approval.')
            return redirect('tips_and_tricks')     
        else:
            messages.error(request, 'Error adding post. Please check the form.')
            return render(request, 'add_post.html', {'form': form})