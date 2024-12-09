from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import (UserCreationForm,
                                       AuthenticationForm,
                                       PasswordResetForm,
                                       SetPasswordForm
                                       )


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "Enter username"
    }))

    password = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "password",
        "placeholder": "Enter password"
    }))


class ResetPasswordForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(ResetPasswordForm, self).__init__(*args, **kwargs)

    email = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "email",
        "placeholder": "enter email-id"
    }))


class NewPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(NewPasswordForm, self).__init__(*args, **kwargs)

    
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': "input",
            "type": "password",
            'autocomplete': 'new-password'
    }))

    new_password2 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': "input",
            "type": "password",
            'autocomplete': 'new-password'
    }))


class UserRegistrationForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "text",
        "placeholder": "Enter Username"
    }))

    email = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "email",
        "placeholder": "Enter Email-id"
    }))

    password1 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "password",
        "placeholder": "Enter Password"
    }))

    password2 = forms.CharField(widget=forms.TextInput(attrs={
        "class": "input",
        "type": "password",
        "placeholder": "Re-enter Password"
    }))
