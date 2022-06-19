from django.db import models
import uuid
from django.forms import BooleanField
from django.contrib.auth.models import User
from product_module.models import Product

# Create your models here.

class PaymentGateway(models.Model):
    token = models.UUIDField(default= uuid.uuid4, editable=False)
    expiry_date = models.DateField()
    balance = models.FloatField()
    is_active = models.BooleanField()
    
# models.UUIDField defines a field for storing universally unique identifiers. It uses Python’s UUID class.

#for invoice

class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.UUIDField()
    payment_date = models.DateTimeField()
    # payment_amount = models.FloatField()
    total_amount = models.FloatField()


class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sub_amount = models.FloatField()