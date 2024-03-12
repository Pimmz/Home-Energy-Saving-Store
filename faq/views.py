from django.views import View
from django.shortcuts import render, redirect
from .models import FAQ
from django.contrib.auth.mixins import LoginRequiredMixin

class FAQView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        
        return render(request, 'faq.html')

    def post(self, request, *args, **kwargs):
    
        if form.is_valid():

            return redirect('success_page')

        else:
           
            return render(request, 'faq.html')
        

# Create your views here.
