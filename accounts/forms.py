from django import forms


class LoginViewModel(forms.Form):
    username = forms.CharField(max_length=120)
    password = forms.CharField(max_length=120)
