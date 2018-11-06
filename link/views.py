# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404,reverse,HttpResponseRedirect
import datetime
from link.models import slink

def index(request):
  if request.method == "POST":
    ten = request.POST.get('linkname','')
    mota = request.POST.get('linkmota','')
    link = request.POST.get('linkurl','')
    l = slink.objects.create(
      LinkName = ten,

      LinkDescription=mota,
      LinkURL = link
    )
    l.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

  else:
    return render(request,'link/index.html',)
