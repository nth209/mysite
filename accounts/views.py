# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404,reverse,HttpResponseRedirect,HttpResponse
from django.contrib.auth.views import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import  PasswordChangeForm
from django.contrib.auth import authenticate, login,update_session_auth_hash
from django.contrib import auth
from django.views import generic
import json

def login(request):
    if request.method=='POST':
       usr = request.POST.get('username','')
       pwd = request.POST.get('pwd','')
       print usr , pwd
       user = auth.authenticate(request,username=usr,password = pwd)
       if user is not None:
           auth.login(request,user)
           return redirect('/home/index')
       else:
           return redirect('/accounts/login')
    else:
        return render(request,'accounts/login.html',)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def loginHome(request):
    if request.method == 'POST':
        usr = request.POST.get('username', '')
        pwd = request.POST.get('pwd', '')
        print usr, pwd
        user = auth.authenticate(request, username=usr, password=pwd)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))