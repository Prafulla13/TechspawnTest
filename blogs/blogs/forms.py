from django.utils.translation import ugettext_lazy as _
from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model
)
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
import re
User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'w-full bg-gray-100 rounded border border-gray-400 focus:outline-none focus:border-indigo-500 text-base px-4 py-2',
                'placeholder': 'Username',
                'required': True,
                'autofocus': True,
            }
        ), label='')
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'w-full bg-gray-100 rounded border border-gray-400 focus:outline-none focus:border-indigo-500 text-base px-4 py-2',
                'placeholder': 'Password',
                'required': True,
            }
        ), label='')

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'w-full bg-gray-100 rounded border border-gray-400 focus:outline-none focus:border-indigo-500 text-base px-4 py-2',
                'placeholder': 'Username',
                'required': True,
                'autofocus': True,
            }
        ), label='')
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'w-full bg-gray-100 rounded border border-gray-400 focus:outline-none focus:border-indigo-500 text-base px-4 py-2',
            'placeholder': 'Email',
            'required': True,
        }
    ), label='')
    email2 = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'w-full bg-gray-100 rounded border border-gray-400 focus:outline-none focus:border-indigo-500 text-base px-4 py-2',
            'placeholder': 'Confirm Email',
            'required': True,
        }
    ), label='')
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'w-full bg-gray-100 rounded border border-gray-400 focus:outline-none focus:border-indigo-500 text-base px-4 py-2',
            'placeholder': 'Password',
            'required': True,
        }
    ), label='')
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'w-full bg-gray-100 rounded border border-gray-400 focus:outline-none focus:border-indigo-500 text-base px-4 py-2',
            'placeholder': 'Confirm Password',
            'required': True,
        }
    ), label='')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',
            'password2'
        ]

    def clean(self, *args, **kwargs):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        email2 = cleaned_data.get('email2')
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if email != email2:
            raise forms.ValidationError('Email must match')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError(
                "This email is already been registered")
        if password != password2:
            raise forms.ValidationError("Password must match")
        if password is not None:
            if not re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
                raise forms.ValidationError(
                    "At least 1 number, 1 Uppercase letter, 1 Special Character and minimum 8 characters required")
