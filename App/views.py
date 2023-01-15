import datetime

from django.shortcuts import render
from App import models

class Users:
    @staticmethod
    def add(name, surname, email):
        item = models.Users(name=name, surname=surname, email=email, date=datetime.date.today())
        item.save()
    @staticmethod
    def get():
        return models.Users.objects.all()
# def add_to_users(name, surname, email):
#     item = models.Users(name=name, surname=surname, email=email, date=datetime.date.today())
#     item.save()
#
# def get_users():
#     return models.Users.objects.all()

def profil(request):
    context = dict()
    context['title'] = 'Настройки профиля'


def index(request):
    Users.add('Leha', 'Mirkin', 'lehamail@gmail.com')
    data = Users.get()
    context = dict()
    context['message'] = 'Пока пусто'
    context['data'] = data


    return render(request, 'index.html', context=context)
