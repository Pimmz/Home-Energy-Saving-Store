from django.shortcuts import render
from django.views import View

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


class BadRequestView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home/400.html', status=400)


class PermissionDeniedView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home/403.html', status=403)


class PageNotFoundView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home/404.html', status=404)


class ServerErrorView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home/500.html', status=500)

