from django import forms


class ProfileEditingForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=50, required=True)
    name = forms.CharField(label='Имя', max_length=50, required=True)
    surname = forms.CharField(label='Фамилия', max_length=50, required=True)


class MakeVotingForm(forms.Form):
    question = forms.CharField(label='Вопрос', max_length=150, required=True)
    vote_variant_1 = forms.CharField(label='Вариант ответа', max_length=50, required=True)
    vote_variant_2 = forms.CharField(label='Вариант ответа', max_length=50, required=True)
    vote_variant_3 = forms.CharField(label='Вариант ответа', max_length=50, required=True)
    vote_variant_4 = forms.CharField(label='Вариант ответа', max_length=50, required=True)