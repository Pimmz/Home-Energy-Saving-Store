from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import TipsAndTricks
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.utils.text import slugify
from django.views.generic.edit import UpdateView, DeleteView



class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = TipsAndTricks
    formm_class = PostForm
    template_name = 'update_post.html'
    success_url = reverse_lazy('tips_and_tricks')
    fields = ['title', 'content', 'featured_image']

class DeletePostView(LoginRequiredMixin, DeleteView):
    model = TipsAndTricks
    success_url = reverse_lazy('tips_and_tricks')


class TipsAndTricksView(View):
    def get(self, request):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                posts = TipsAndTricks.objects.all().order_by('-created_at')
            else:
                posts = TipsAndTricks.objects.filter(is_approved=True).order_by('-created_at')

            paginator = Paginator(posts, 6)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

            return render(request, 'tips_and_tricks.html', {'page_obj': page_obj})
        else:
            messages.error(request, 'You must be logged in to view this page.')
            return redirect('account_login')

class AddPostView(LoginRequiredMixin, View):
    def get(self, request):
        form = PostForm()
        return render(request, 'add_post.html', {'form':form})

    def post (self, request):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug = slugify(post.title)
            post.save()
            messages.success(request, 'Post added successfully. Waiting for Approval.')
            return redirect('tips_and_tricks')     
        else:
            messages.error(request, 'Error adding post. Please check the form.')
            return render(request, 'add_post.html', {'form': form})