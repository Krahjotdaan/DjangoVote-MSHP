from django import forms


class ProfileEditingForm(forms.Form):
    email = forms.EmailField(label='email', max_length=50, required=True)
    name = forms.CharField(label='имя', max_length=50, required=True)

class VotingForm(forms.Form):
    title = forms.CharField(label='Название голосования', max_length=50, required=True)
    description = forms.CharField(label='Описание голосования', max_length=100, required=True)
    variants = forms.CharField(label='варианты ответов (разделяются Enter\'ом)', max_length=300, required=True)

class VariantForm(forms.Form):
    variant = forms.RadioSelect()