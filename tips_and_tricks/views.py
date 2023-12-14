from django.views import View
from django.shortcuts import render, redirect
from .models import TipsAndTricks

class TipsAndTricksView(View):
    def get(self, request, *args, **kwargs):
        
        return render(request, 'tips.html')

    def post(self, request, *args, **kwargs):
    
        if form.is_valid():

            return redirect('success_page')

        else:
           
            return render(request, 'tips.html')
        

# Create your views here.
