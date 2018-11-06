# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

# Create your models here.

class userProfile(models.Model):
    userProfileID = models.AutoField(primary_key=True)
    user = models.OneToOneField(User)
    userProfilenPhone = models.IntegerField("Số điện thoại")
    userProfileLocal = models.TextField("Địa chỉ", max_length=1000)
    userProfileIdentity = models.IntegerField("Số chứng minh nhân dân")
    userProfilePermission = models.IntegerField("Quyền truy cập", default=3) # 1 superuser 2 admin, 3 user
    def __str__(self):
        return self.user.username.encode('utf8')