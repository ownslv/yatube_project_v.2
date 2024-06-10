from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template = 'posts/index.html'
    return render(request, template)


def group_posts(request, slug):
    return HttpResponse(f'Группа - {slug}')
