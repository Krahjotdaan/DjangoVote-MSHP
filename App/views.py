from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render
from App import models
from App.forms import ProfileEditingForm
from App.forms import VotingForm2Variants, VotingForm3Variants, VotingForm4Variants


@login_required
def profile_page(request):
    context = dict()
    context['title'] = 'Настройки профиля'
    context['uservotings'] = models.VotedVoting.objects.all()
    return render(request, 'profile/index.html', context)


def index(request):
    context = dict()
    if request.user.username == "":
        messages.info(request, 'Вы вышли из аккаунта')
    else:
        messages.success(request, 'Вы успешно вошли в аккаунт')

    return render(request, 'index.html', context=context)


@login_required
def profile_editing(request):
    context = dict()

    if request.method == 'POST':
        form = ProfileEditingForm(request.POST)

        if form.is_valid() and (request.user.username != form.data['name'] or request.user.email != form.data['email']):
            name = form.data['name']
            email = form.data['email']
            request.user.username = name
            request.user.email = email
            request.user.save()
            messages.success(request, 'Профиль успешно изменен')
        else:
            context['form'] = form
            messages.warning(request, 'Нет изменений')

    else:
        context['nothing_entered'] = True
        context['form'] = ProfileEditingForm()

    context['form'] = ProfileEditingForm()

    return render(request, 'profile/edit.html', context=context)


@login_required
def make_voting(request):
    context = dict()
    context['userita'] = request.user.id
    varsa = request.GET.get('vars', 2)
    context['test'] = varsa
    form = None

    if type(varsa) == 'NoneType':
        varsa = 2
    varsa = int(varsa)

    if request.method == 'POST':
        if varsa == 2:
            form = VotingForm2Variants(request.POST)
        if varsa == 3:
            form = VotingForm3Variants(request.POST)
        if varsa == 4:
            form = VotingForm4Variants(request.POST)

        if form.is_valid():
            title = form.data['title']
            desc = form.data['description']

            item = models.Voting(title=title, description=desc, author=request.user)
            item.save()

            if varsa == 2:
                variant1 = form.data['variant1']
                variant2 = form.data['variant2']
                models.VoteVariant.objects.create(description=variant1, voting_id=item)
                models.VoteVariant.objects.create(description=variant2, voting_id=item)
            if varsa == 3:
                variant1 = form.data['variant1']
                variant2 = form.data['variant2']
                variant3 = form.data['variant3']
                models.VoteVariant.objects.create(description=variant1, voting_id=item)
                models.VoteVariant.objects.create(description=variant2, voting_id=item)
                models.VoteVariant.objects.create(description=variant3, voting_id=item)
            if varsa == 4:
                variant1 = form.data['variant1']
                variant2 = form.data['variant2']
                variant3 = form.data['variant3']
                variant4 = form.data['variant4']
                models.VoteVariant.objects.create(description=variant1, voting_id=item)
                models.VoteVariant.objects.create(description=variant2, voting_id=item)
                models.VoteVariant.objects.create(description=variant3, voting_id=item)
                models.VoteVariant.objects.create(description=variant4, voting_id=item)

            messages.success(request, 'Голосование успешно создано')

        else:
            context['form'] = form

    else:
        context['nothing_entered'] = True
        # = VotingForm2Variants()
        # context['form'] = VotingForm2Variants()
        if varsa == 2:
            context['form'] = VotingForm2Variants()
        if varsa == 3:
            context['form'] = VotingForm3Variants()
        if varsa == 4:
            context['form'] = VotingForm4Variants()

    if varsa == 2:
        context['form'] = VotingForm2Variants()
    if varsa == 3:
        context['form'] = VotingForm3Variants()
    if varsa == 4:
        context['form'] = VotingForm4Variants()

    return render(request, 'votings/create.html', context)


'''
def votings_list_page(request):
    votings = models.Voting.objects.all().order_by('-id')
    variants = models.VoteVariant.objects.all()
    votings_voted = [False] * len(votings)
    for i in range(len(votings)):
        if votings[i].is_voted(request.user, votings[i]):
            votings_voted[i] = True

    context = {
        'votings': votings,
        'variants': variants,
        'voted_voting': models.VotedVoting.objects.all(),
    }

    ids = []
    two_var = []
    for i in variants:
        ids.append(i.voting_id)
    for i in ids:
        if ids.count(i) == 2:
            two_var.append(i)
    context["voting_with_2_var"] = two_var

    get_variant = request.GET.get('variant', 0)
    facts = models.VoteFact.get_facts_by_user(request.user)
    context['userita'] = request.user

    # ↓↓↓ проверка на повторный отзыв ↓↓↓
    to_publicate = True
    if get_variant != 0:
        get_variant = models.VoteVariant.objects.filter(id=get_variant)[0]
        for i in facts:
            if i.variant.voting_id == get_variant.voting_id:
                to_publicate = False
                messages.warning(request, 'Нельзя голосовать дважды')
                break

        if to_publicate:
            models.VoteFact.objects.create(author=request.user, variant=get_variant)
            messages.success(request, 'Вы успешно проголосовали')
    context['to_publicate'] = to_publicate

    return render(request, 'votings/list.html', context)
'''


def votings_list_page(request):
    votings = models.Voting.objects.all().order_by('-id')
    variants = models.VoteVariant.objects.all()
    votings_voted = [False] * len(votings)
    for i in range(len(votings)):
        if votings[i].is_voted(request.user, votings[i]):
            votings_voted[i] = True

    context = {
        'votings': votings,
        'variants': variants,
        'voted_voting': models.VotedVoting.objects.all(),
    }

    ids = []  # id всех вариантов ответов
    two_var = []  # id вариантов ответов ( добавить если в голосовании их только два)
    for i in variants:
        ids.append(i.voting_id)
    for i in ids:
        if ids.count(i) == 2:
            two_var.append(i)
    context["voting_with_2_var"] = two_var

    get_variant = request.GET.get('variant', 0)
    facts = models.VoteFact.get_facts_by_user(request.user)
    context['userita'] = request.user

    # ↓↓↓ проверка на повторный отзыв ↓↓↓
    to_publicate = True
    #
    # if answer != 0:
    #     for i in models.VoteFact.get_facts_by_user(request.user):
    #         if models.VoteVariant.objects.filter(id=answer)[0].voting_id == i.variant.voting_id:
    if (get_variant != 0):
        get_variant = models.VoteVariant.objects.filter(id=get_variant)[0]  # меняю айди варианта на объект варианта
        for i in facts:  # пробегаюсь по всем голосам юзера и проверяю относится ли один из них к голосованию текущего варианта
            if i.variant.voting_id == get_variant.voting_id:
                to_publicate = False
                messages.warning(request, 'Нельзя голосовать дважды')
                break
        # if answer != 0 and to_publicate is True:
        #     models.VoteFact.objects.create(author=request.user, variant=models.VoteVariant.objects.filter(id=answer)[0])
        #     messages.success(request, 'Вы успешно проголосовали')

        if to_publicate:  # если все в порядке, публикую
            # models.VotedVoting.objects.create(author=request.user, voting=get_variant.voting_id) # создаю VotedVoting
            models.VoteFact.objects.create(author=request.user, variant=get_variant)  # создаю VoteFact
            messages.success(request, 'Вы успешно проголосовали')
    context['to_publicate'] = to_publicate

    return render(request, 'votings/list.html', context)
