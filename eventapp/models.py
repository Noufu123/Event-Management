from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class usermodel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    user_Photo=models.ImageField(null=True,blank=True,upload_to='image/')
    user_address=models.CharField(max_length=250)
    user_number=models.IntegerField()


class productmodel(models.Model):
    product_photo=models.ImageField(null=True,blank=True,upload_to='image/')
    prdct=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    product_name=models.CharField(max_length=250)
    product_price=models.IntegerField()


class servicemodel(models.Model):
    Ser_Photo=models.ImageField(null=True,blank=True,upload_to='image/')
    ser=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    Ser_Name=models.CharField(max_length=25)
    Ser_Price=models.IntegerField()
    
class bookmodel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    prdct=models.ForeignKey(productmodel,on_delete=models.CASCADE,null=True)
    ser=models.ForeignKey(servicemodel,on_delete=models.CASCADE,null=True)

class bookdatemodel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    prdct=models.ForeignKey(productmodel,on_delete=models.CASCADE,null=True)
    ser=models.ForeignKey(servicemodel,on_delete=models.CASCADE,null=True)
    date=models.DateField(auto_now_add=True)
