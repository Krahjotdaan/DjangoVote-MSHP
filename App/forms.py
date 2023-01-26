from django import forms


class ProfileEditingForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=50, required=True)
    name = forms.CharField(label='Имя', max_length=50, required=True)
    surname = forms.CharField(label='Фамилия', max_length=50, required=True)
