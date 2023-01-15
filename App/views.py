import datetime

from django.shortcuts import render
from App import models
from App.tables_classes.Users import Users

def profil(request):
    context = dict()
    context['title'] = 'Настройки профиля'

def index(request):
    Users.add('Leha2', 'Mirkin', 'lehamail@gmail.com')
    data = Users.get()

    context = dict()
    context['message'] = 'Пока пусто'
    context['data'] = data


    return render(request, 'index.html', context=context)
