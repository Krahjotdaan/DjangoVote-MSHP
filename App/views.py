import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from App import models
from App.tables_classes.Users import Users
from App.forms import ProfileEditingForm, VotingForm
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
            email = form.data['email']
            request.user.username = name
            request.user.email = email
            #todo сделать чтобы изменялся весь пользователь
        else:
            context['form'] = form

    else:
        context['nothing_entered'] = True
        context['form'] = ProfileEditingForm()
    context['form'] = ProfileEditingForm()

    return render(request, 'profile_editing.html', context=context)

def votings(request):
    data = models.Voting.objects.all()
    data = list(reversed(data))
    variants = models.VoteVariant.objects.all()
    context = {
        'data': data,
        'variants': variants,
    }
    return render(request, 'voting_page.html', context)
@login_required
def make_voting(request):
    context = dict()
    context['userita'] = request.user.id
    context['test'] = 'asdf'

    if request.method == 'POST':
        form = VotingForm(request.POST)

        if form.is_valid():
            title = form.data['title']
            variants = form.data['variants']
            desc = form.data['description']

            item = models.Voting(title=title, description=desc, author=request.user)
            item.save()
            models.VoteVariant.objects.create(description=variants, voting_id=item)
        else:
            context['form'] = form

    else:
        context['nothing_entered'] = True
        context['form'] = VotingForm()
    context['form'] = VotingForm()
    return render(request, 'make_voting.html', context)