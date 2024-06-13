from django.shortcuts import render
from .models import Post


def index(request):
    template = 'posts/index.html'
    tittle = "Главная страница Yatube"
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        "tittle": tittle,
        "posts": posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    tittle = "Здесь будет информация о группах проекта Yatube"
    context = {
        "tittle": tittle,
    }
    return render(request, template, context)
