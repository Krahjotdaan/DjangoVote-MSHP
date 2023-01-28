from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from App.models import Profile


def profil(request):
    context = dict()
    context['title'] = 'Настройки профиля'
    return render(request, 'profil.html', context=context)


def index(request):
    context = dict()
    context['message'] = 'Пока пусто'
    return render(request, 'index.html', context=context)