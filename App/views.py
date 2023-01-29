import datetime

from django.shortcuts import render
from App import models
from App.tables_classes.Users import Users
from App.forms import MakeVotingForm
def profil(request):
    context = dict()
    context['title'] = 'Настройки профиля'
    return render(request, 'profil.html', context)

def index(request):

    context = dict()
    context['message'] = 'Пока пусто'


    return render(request, 'index.html', context=context)


def profile_editing(request):

    context = dict()

    if request.method == 'POST':
        form = ProfileEditingForm(request.POST)

        if form.is_valid():
            name = form.data['name']
            surname = form.data['surname']
            email = form.data['email']
            user_id = request.user.id
            # а как обновлять тo????????????
        else:
            context['form'] = form

    else:
        context['nothing_entered'] = True
        context['form'] = ProfileEditingForm()

    return render(request, 'profile_editing.html', context=context)

def make_voting(request):
    context = dict()

    if request.method == 'POST':
        form = MakeVotingForm(request.POST)

        if form.is_valid():
            context['form'] = form
        else:
            context['form'] = ''

    else:
        context['nothing_entered'] = True
        context['form'] = MakeVotingForm()
    return render(request, 'voting_page.html', context=context)

def votings(request):
    return render(request, 'voting_page.html')