from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Newsletter
from .forms import NewsletterForm


def newsletter_view(request):
    form = NewsletterForm(request.POST or None)

    if request.method == "POST":
        email = request.POST.get('email')
        if Newsletter.objects.filter(email=email).exists():
            messages.error(request, 'You are already subscribed')
            return redirect('newsletter')
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks for signing upto our newsletter')
            return redirect('newsletter')
        messages.error(request, 'Error please try again!')
    context = {'form': form}
    return render(request, 'newsletter.html', context)
    