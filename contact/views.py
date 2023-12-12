from django.shortcuts import render, redirect
from django.views import View
from .forms import ContactForm

# Create your views here.


class ContactView(View):
    def get(self, request, *args, **kwargs):
        context = {'form': ContactForm()}
        return render(request, 'contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():

            return redirect('success_page')

        else:
            context = {'form': form}
            return render(request, 'contact.html', context)
