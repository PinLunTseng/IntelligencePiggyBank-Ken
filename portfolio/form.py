from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class CreateUserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    email = forms.EmailField
