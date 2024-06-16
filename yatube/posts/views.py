from django.shortcuts import render, get_object_or_404
from .models import Post, Group

header = "| Lenta"


def index(request):
    template = 'posts/index.html'
    tittle = "Lenta Yatube"
    tittle_group = Group.objects.all()
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        "tittle": tittle,
        "posts": posts,
        "header": header,
        "tittle_group" : tittle_group,
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    template = 'posts/group_list.html'
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        "group": group,
        "posts": posts,
        "header": header,
    }
    return render(request, template, context)
