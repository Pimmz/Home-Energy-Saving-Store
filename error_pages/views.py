from django.shortcuts import render
from django.views import View
from django.http import HttpResponseNotFound, HttpResponseServerError, HttpResponseForbidden, HttpResponseBadRequest

# Create your views here.

class CustomBadRequestView(View):
    def get(self, request, exception=None):
        return render(request, 'error/400.html', status=400)

class CustomPermissionDeniedView(View):
    def get(self, request, exception=None):
        return render(request, 'error/403.html', status=403)

class CustomPageNotFoundView(View):
    def get(self, request, exception=None):
        return render(request, 'error/404.html', status=404)

class CustomServerErrorView(View):
    def get(self, request, exception=None):
        return render(request, 'error/500.html', status=500)
