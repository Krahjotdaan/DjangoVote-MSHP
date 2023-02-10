from django import forms


class ProfileEditingForm(forms.Form):
    email = forms.EmailField(label='email', max_length=50, required=True)
    name = forms.CharField(label='имя', max_length=50, required=True)


class VotingForm2Variants(forms.Form):
    title = forms.CharField(label='Название голосования', max_length=50, required=True)
    description = forms.CharField(label='Описание голосования', max_length=100, required=True)
    variant1 = forms.CharField(label='вариант ответa 1', max_length=300, required=True)
    variant2 = forms.CharField(label='вариант ответa 2', max_length=300, required=True)


class VotingForm3Variants(forms.Form):
    title = forms.CharField(label='Название голосования', max_length=50, required=True)
    description = forms.CharField(label='Описание голосования', max_length=100, required=True)
    variant1 = forms.CharField(label='вариант ответa 1', max_length=300, required=True)
    variant2 = forms.CharField(label='вариант ответa 2', max_length=300, required=True)
    variant3 = forms.CharField(label='вариант ответa 3', max_length=300, required=True)


class VotingForm4Variants(forms.Form):
    title = forms.CharField(label='Название голосования', max_length=50, required=True)
    description = forms.CharField(label='Описание голосования', max_length=100, required=True)
    variant1 = forms.CharField(label='вариант ответa 1', max_length=300, required=True)
    variant2 = forms.CharField(label='вариант ответa 2', max_length=300, required=True)
    variant3 = forms.CharField(label='вариант ответa 3', max_length=300, required=True)
    variant4 = forms.CharField(label='вариант ответa 4', max_length=300, required=True)


class VariantForm(forms.Form):
    variant = forms.RadioSelect()


class MakeVotingForm(forms.Form):
    question = forms.CharField(label='Вопрос', max_length=150, required=True)
    vote_variant_1 = forms.CharField(label='Вариант ответа', max_length=50, required=True)
    vote_variant_2 = forms.CharField(label='Вариант ответа', max_length=50, required=True)
    vote_variant_3 = forms.CharField(label='Вариант ответа', max_length=50, required=True)
    vote_variant_4 = forms.CharField(label='Вариант ответа', max_length=50, required=True)
