from email.mime import image
from statistics import mode
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils.html import mark_safe

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField()
    


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