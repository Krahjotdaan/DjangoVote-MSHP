import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from App import models
from App.tables_classes.Users import Users
from App.forms import ProfileEditingForm, VotingForm, VariantForm

from App.forms import MakeVotingForm, ProfileEditingForm


def profile_page(request):
    context = dict()
    context['title'] = 'Настройки профиля'
    return render(request, 'profile/index.html', context)


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
            # todo сделать чтобы изменялся весь пользователь
        else:
            context['form'] = form

    else:
        context['nothing_entered'] = True
        context['form'] = ProfileEditingForm()
    context['form'] = ProfileEditingForm()

    return render(request, 'profile/edit.html', context=context)


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
    return render(request, 'votings/create.html', context=context)


def voting_page_template(request):
    return render(request, 'votings/details_template.html')


def votings(request):
    data = models.Voting.objects.all()
    data = list(reversed(data))
    variants = models.VoteVariant.objects.all()
    context = {
        'data': data,
        'variants': variants,
    }
    answer = request.GET.get('variant', 0)
    to_publicate = True
    if answer != 0:
        for i in models.VoteFact.get_facts_by_user(request.user):
            if models.VoteVariant.objects.filter(id=answer)[0].voting_id == i.variant.voting_id:
                to_publicate = False
    if answer != 0 and to_publicate:
        models.VoteFact.objects.create(author=request.user, variant=models.VoteVariant.objects.filter(id=answer)[0])
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
