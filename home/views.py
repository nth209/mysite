# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404,reverse,HttpResponseRedirect

from django.contrib.auth.views import login
from django.contrib.auth.models import User

from django.contrib.auth.forms import  PasswordChangeForm
from django.contrib.auth import authenticate, login,update_session_auth_hash
from django.contrib import auth
from django.views import generic
from home.models import tyleProduct,product,brandProduct,menuNgang
from django.core.paginator import Paginator


def index(request):
    menu = menuNgang.objects.all().order_by('menuID')
    arg = {'menu':menu}
    return render(request,'home/index.html',arg)