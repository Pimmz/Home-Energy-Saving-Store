from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contact_view(request):
    form = ContactForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact Form Submitted Successfully!')
            return redirect('contact')
        messages.error(request, 'Error please try again!')
    context = {'form': form}
    return render(request, 'contact.html', context)
