from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.shortcuts import render
from django.views import View


# Create your views here.

class custom_400(View):
    """
    View for the 400 error page
    """
    def dispatch(self, request, exception=None):
        return render(request, 'templates/400.html', status=400)


class custom_403(View):
    """
    View for the 403 error page
    """
    def dispatch(self, request, exception=None):
        return render(request, 'templates/403.html', status=403)


class custom_404(View):
    """
    View for the 404 error page
    """
    def dispatch(self, request, exception=None):
        return render(request, 'templates/404.html', status=404)


class custom_500(View):
    """
    View for the 500 error page
    """
    def dispatch(self, request, exception=None):
        return render(request, 'templates/500.html', status=500)
