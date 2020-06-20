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


class blog_form(forms.Form):
    blog_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'w-full bg-gray-100 rounded border border-gray-400 focus:outline-none focus:border-indigo-500 text-base px-4 py-2',
                'placeholder': 'Title',
            }
        ), label='')
    blog_content = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'w-full bg-gray-100 rounded border border-gray-400 focus:outline-none h-48 focus:border-indigo-500 text-base px-4 py-2 resize-none block',
                'placeholder': 'Message',
            }
        ), label='')
    blog_tech = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'w-full bg-gray-100 rounded border border-gray-400 focus:outline-none focus:border-indigo-500 text-base px-4 py-2',
                'placeholder': 'Technology',
            }
        ), label='')
