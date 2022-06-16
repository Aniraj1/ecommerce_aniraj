from email.mime import image
from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils.html import mark_safe

#User model is default Django authorization
from django.contrib.auth.models import User

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField()
    
    def __str__(self):
        return self.name
    


class Category(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField()
    
    class Meta:
        verbose_name_plural = "Categories"   #To rename the name

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    quantity = models.IntegerField()
    image_url = models.CharField(max_length=500)
    color_code = models.CharField(max_length=20, default= "")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    registered_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField()
    
    
    def image_tag(self):
        return mark_safe(f'<img src="{self.image_url}" width="50" height="50" />')
        image_tag.short_description = "Product" 
       
    
    # it writes it's own name
    def __str__(self):
        return self.name
    


# TODO: Add Cart_item

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    entered_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Cart_Items"
    
    def __str__(self):
        return self.product


