from django.shortcuts import render


def index(request):
    template = 'posts/index.html'
    tittle = "Это главная страница проекта Yatube"
    context = {
        "tittle": tittle,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    tittle = "Здесь будет информация о группах проекта Yatube"
    context = {
        "tittle": tittle,
    }
    return render(request, template, context)
