from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class CreateUserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    email = forms.EmailField()


class RiskPreferenceMeasureForm01(forms.Form):
    question01_01 = forms.CharField()
    question01_02 = forms.CharField()
    question01_03 = forms.ChoiceField()


class RiskPreferenceMeasureForm02(forms.Form):
    question02_01 = forms.CharField()
    question02_02 = forms.CharField()