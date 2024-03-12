from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import TipsAndTricks, ApprovalStatus
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.utils.text import slugify
from django.views.generic.edit import UpdateView, DeleteView



class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = TipsAndTricks
    form_class = PostForm
    template_name = 'update_post.html'
    success_url = reverse_lazy('tips_and_tricks')

    def form_valid(self,form):
        messages.success(self.request, 'Post Updated Successfully!')
        return super().form_valid(form)

class DeletePostView(LoginRequiredMixin, DeleteView):
    model = TipsAndTricks
    success_url = reverse_lazy('tips_and_tricks')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Post Deleted Successfully!')
        return super().delete(request, *args, **kwargs)

class TipsAndTricksView(View):
    def get(self, request):
        if request.user.is_authenticated:
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
            post.is_approved =False
            post.save()
            messages.success(request, 'Post added successfully. Waiting for Approval.')
            return redirect('tips_and_tricks')     
        else:
            messages.error(request, 'Error adding post. Please check the form.')
            return render(request, 'add_post.html', {'form': form})