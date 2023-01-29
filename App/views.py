from django.shortcuts import render

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
            surname = form.data['surname']
            email = form.data['email']
            user_id = request.user.id
            # а как обновлять тo????????????
        else:
            context['form'] = form

    else:
        context['nothing_entered'] = True
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
