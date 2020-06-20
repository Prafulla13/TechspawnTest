from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    authenticate,
    get_user_model,
    logout,
    login
)
from rest_framework import generics, status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .forms import UserRegisterForm, UserLoginForm
from django.contrib import messages
from blogs.profile_form import profile_form
from blogger.models import blogs
from blogs.blog_form import blog_form
from django.views.decorators.csrf import csrf_protect
import datetime
from blogger.blogger_serializer import BlogSerializer
from django.http import JsonResponse


def index(request):
    if request.method == 'GET':
        dataList = []
        blog_obj = blogs.objects.all()
        for blogData in blog_obj:
            data = {'blog_name': blogData.blog_name,
                    'blog_content': blogData.blog_body,
                    'blog_tech': blogData.blog_technology}
            form = blog_form(data)
            dataList.append(form)
        return render(request, "index.html", {'form': dataList})
    elif request.method == 'POST':
        form = blog_form(request.POST)
        print("----", form)
        if form.is_valid():
            blog_name = form.cleaned_data.get('blog_name')
            blog_content = form.cleaned_data.get('blog_content')
            blog_tech = form.cleaned_data.get('blog_tech')
            blog_data = {
                'blog_name': blog_name,
                'blog_body': blog_content,
                'blog_technology': blog_tech,
                'status': 1,
                'user': request.user.id,
                'created_by': request.user.id,
                'created_on': datetime.datetime.now()}
            # calling the BlogSerializer
            serializer = BlogSerializer(data=blog_data)
            print(serializer)
            if serializer.is_valid():
                serializer.save()
            else:
                Response(serializer.errors)
            return redirect('/')
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})


@login_required(login_url='/login')
def profile(request):
    return render(request, 'profile.html', {})


def login_function(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    else:
        form = UserLoginForm()
    return render(request, "login.html", {'form': form})


def logout_function(request):
    logout(request)
    return redirect('/')


@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            new_user = authenticate(username=user.username, password=password)
            login(request, new_user)
            return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request, "register.html", {'form': form})


def contact(request):
    return render(request, 'contact.html', {})


@login_required(login_url='/login')
def profile_info(request):
    user_id = request.user.id
    user_obj = User.objects.get(id=user_id)
    data = {'fname': user_obj.first_name,
            'lname': user_obj.last_name,
            'email': user_obj.email}
    if request.method == 'GET':
        form = profile_form(data)
        print('Form', form)

    # if request.method == 'POST':
    #     form = UserLoginForm(request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data.get('username')
    #         password = form.cleaned_data.get('password')
    #         user = authenticate(username=username, password=password)
    #         if user is not None:
    #             login(request, user)
    #             return redirect('/')
    return render(request, "profile.html", {'form': form})
