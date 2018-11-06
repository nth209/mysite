# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime
from django.contrib.auth.models import User
from accounts.models import userProfile

class menuNgang(models.Model):
    menuID = models.AutoField(primary_key=True)
    menuTen = models.CharField("Tên Menu", max_length=255, unique=True)
    def __str__(self):
        return self.menuTen.encode('utf8')

class contact(models.Model):
    contactID = models.AutoField(primary_key=True)
    contactName = models.CharField("Họ tên",max_length=255,blank=True)
    contactEmail = models.EmailField("Email", max_length=255)
    contactPhone = models.IntegerField(default=0)
    contactContent = models.TextField("Nội dung", max_length=1000, blank=True)
    user = models.ForeignKey(User)


class brandProduct(models.Model):
    brandID = models.AutoField(primary_key=True)
    brandName = models.CharField("Tên hảng sản xuất",max_length=255,unique=True)
    def __str__(self):
        return self.brandName.encode('utf8')

class tyleProduct(models.Model):
    typeID = models.AutoField(primary_key=True)
    typeName = models.CharField("Tên Loại sản phẩm", max_length=255,unique=True)

    def __str__(self):
        return self.typeName.encode('utf8')

class product(models.Model):
    productID = models.AutoField(primary_key=True)
    productCode = models.CharField("Mã sản phẩm", max_length=255,unique=True)
    productName = models.CharField("Tên sản phẩm",max_length=400, blank=True)
    productPrice = models.IntegerField()
    productPricePro = models.IntegerField() #gia khuyen mai
    productQuantity = models.IntegerField()
    productDescription = models.TextField("Thông tin chi tiết", max_length=1000)
    productPromotion = models.BooleanField("Chương trình khuyến mãi",default=False) # chương trinh khuyen mai
    productHot = models.BooleanField("Sản phẩm hot",default=False)
    productActive = models.BooleanField("Active",default=False)
    producImg = models.ImageField("Ảnh sản phẩm", upload_to="product/%Y/%m/%d")
    productCreate = models.DateField(default=datetime.date.today)
    productTyle = models.ForeignKey(tyleProduct)
    productBrand = models.ForeignKey(brandProduct)
    def __str__(self):
        return self.productName.encode('utf8')

class pay(models.Model): #don hang
    payID = models.AutoField(primary_key=True)
    payDate = models.DateField(default=datetime.date.today)
    payName = models.ForeignKey(User)
    payTotal = models.IntegerField()


class payDetail(models.Model): # chi tiet don hang , bang phu
    pay = models.ForeignKey(pay)
    payProduct = models.ForeignKey(product)
    payQuantity = models.IntegerField()



class event(models.Model): #su kien
    eventID = models.AutoField(primary_key=True)
    eventImg = models.ImageField("ảnh đại diện",upload_to="event/%Y/%m/%d")
    eventDetail = models.TextField("Chi tiết sự kiện", max_length=1000)
    eventCreated = models.DateField(default=datetime.date.today)
    eventActive = models.BooleanField(default=False)