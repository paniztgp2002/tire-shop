from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)
    balance = models.IntegerField(default=0)
    def last_address(self):
        return CustomerHasCart.objects.filter(customer_id=self.id).latest('address')
    def last_postcode(self):
        return CustomerHasCart.objects.filter(customer_id=self.id).latest('postcode')

class Cart(models.Model):
    adress = models.CharField(max_length=200)
    Paid = models.BooleanField()
    DateTime= models.DateField(auto_now_add=False)
    Postcode = models.CharField(max_length=20)
    #totalprice

class CustomerHasCart(models.Model):
    customer_id = models.IntegerField()
    cart_id = models.IntegerField()
class Product(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=30)
class Tube(models.Model):
    size = models.CharField(max_length=5)
class Tire(models.Model):
    description = models.CharField(max_length=200)
    layer = models.CharField(max_length=20)
    pattern = models.CharField(max_length=20)
class rime(models.Model):
    description = models.CharField(max_length=5)
    layer = models.CharField(max_length=20)
    pattern = models.CharField(max_length=20)
class Seller(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)
    balance = models.IntegerField(default=0)
class Organization(models.Model):
    name = models.CharField(max_length=50)
                     
