from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from App import models
from App.forms import ProfileEditingForm
from App.forms import VotingForm2Variants


def profile_page(request):
    context = dict()
    context['title'] = 'Настройки профиля'
    return render(request, 'profile/index.html', context)


def index(request):
    context = dict()
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


@login_required
def make_voting(request):
    context = dict()
    context['userita'] = request.user.id
    # varsa = request.GET.get('vars')
    # context['test'] = varsa
    if request.method == 'POST':

        form = VotingForm2Variants(request.POST)

        if form.is_valid():
            title = form.data['title']
            variant1 = form.data['variant1']
            variant2 = form.data['variant2']
            desc = form.data['description']

            item = models.Voting(title=title, description=desc, author=request.user)
            item.save()
            models.VoteVariant.objects.create(description=variant1, voting_id=item)
            models.VoteVariant.objects.create(description=variant2, voting_id=item)
        else:
            context['form'] = form

    else:
        context['nothing_entered'] = True
        context['form'] = VotingForm2Variants()
    context['form'] = VotingForm2Variants()
    return render(request, 'votings/create.html', context)


def votings_list_page(request):
    data = models.Voting.objects.all().order_by('-id')
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
    return render(request, 'votings/list.html', context)
