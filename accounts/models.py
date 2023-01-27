from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=20,null=True)
    email = models.CharField(max_length=60,null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.phone}"


class Tag(models.Model):
    name = models.CharField(max_length=100,null=True)

    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    CATEGORY = (
        ('Indoor','Indoor'),
        ('Outdoor','Outdoor'),
    )
    name = models.CharField(max_length=200,null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2,default=0.0)
    category = models.CharField(max_length=50,null=True,choices=CATEGORY)
    description = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.name} {self.price} {self.category}"



class Order(models.Model):
    STATUS = (
        ('Pending','Pending'),
        ('Out For Delivery','Out for delivery'),
        ('Delivered','Delivered'),
    )
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,null=True,choices=STATUS)
    note = models.CharField(max_length=1000,null=True)

    def __str__(self):
        return f"{self.customer} {self.status}"


