from django.shortcuts import render


def profil(request):
    context = dict()
    context['title'] = 'Настройки профиля'
    return render(request, 'profil.html', context=context)


def index(request):
    context = dict()
    context['message'] = 'Пока пусто'
    return render(request, 'index.html', context=context)