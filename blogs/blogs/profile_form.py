from django.utils.translation import ugettext_lazy as _
from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model
)
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
import re
from django.contrib.auth.models import User
from blogger.models import blogs
User = get_user_model()


class profile_form(forms.Form):
    fname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'w-full bg-gray-100 rounded border border-gray-400 focus:outline-none focus:border-indigo-500 text-base px-4 py-2',
                'placeholder': 'First Name',
            }
        ), label='')
    lname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'w-full bg-gray-100 rounded border border-gray-400 focus:outline-none focus:border-indigo-500 text-base px-4 py-2',
                'placeholder': 'Last Name',
            }
        ), label='')
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'w-full bg-gray-100 rounded border border-gray-400 focus:outline-none focus:border-indigo-500 text-base px-4 py-2',
            'placeholder': 'Email',
            'required': True,
        }
    ), label='')
