from django.shortcuts import render


def profil(request):
    context = dict()
    context['title'] = 'Настройки профиля'


def index(request):
    context = dict()
    context['massage'] = 'Пока пусто'

    return render(request, 'index.html', context=context)
