# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from home.models import tyleProduct,brandProduct,product,pay,payDetail,contact,event, menuNgang
admin.site.register(tyleProduct)
admin.site.register(brandProduct)
admin.site.register(product)
admin.site.register(contact)
admin.site.register(event)
admin.site.register(payDetail)
admin.site.register(pay)
admin.site.register(menuNgang)
# Register your models here.
