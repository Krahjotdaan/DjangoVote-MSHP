import datetime

from django.shortcuts import render
from App import models

def add_to_users(name, surname, email):
    item = models.Users(name=name, surname=surname, email=email, date=datetime.date.today())
    item.save()

def get_users():
    return models.Users.objects.all()

def profil(request):
    context = dict()
    context['title'] = 'Настройки профиля'


def index(request):
    add_to_users('Leha', 'Mirkin', 'lehamail@gmail.com')
    data = get_users()
    context = dict()
    context['message'] = 'Пока пусто'
    context['data'] = data


    return render(request, 'index.html', context=context)
