from django.shortcuts import render
from .forms import ProfileEditingForm


def profile(request):
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