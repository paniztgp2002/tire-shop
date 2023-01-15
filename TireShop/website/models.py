from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)
    balance = models.IntegerField(default=0)
    def last_address(self):
        return Cart.objects.filter(customer_id=self.id).latest('address')
    def last_postcode(self):
        return Cart.objects.filter(customer_id=self.id).latest('postcode')


class Cart(models.Model):
    adress = models.CharField(max_length=200)
    paid = models.BooleanField()
    datetime = models.DateField(auto_now_add=False)
    postcode = models.CharField(max_length=20)
    customer_id = models.IntegerField()
    #totalprice


class CartContainsProduct(models.Model):
    quantity = models.IntegerField(default=1)
    cart_id = models.IntegerField()
    product_id = models.IntegerField()


class Product(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=30)
    seller_id = models.IntegerField()
    quantity = models.IntegerField(default=0)
    price = models.IntegerField()


class DealContainsProduct(models.Model):
    quantity = models.IntegerField(default=1)
    deal_id = models.IntegerField()
    product_id = models.IntegerField()


class Deal(models.Model):
    datetime = models.DateField(auto_now_add=False)
    seald = models.BooleanField()


class Tube(models.Model):
    size = models.CharField(max_length=5)


class Tire(models.Model):
    description = models.CharField(max_length=200)
    layer = models.CharField(max_length=20)
    pattern = models.CharField(max_length=20)


class Rim(models.Model):
    description = models.CharField(max_length=5)
    layer = models.CharField(max_length=20)
    pattern = models.CharField(max_length=20)    


class Organization(models.Model):    
    name = models.CharField(max_length=50)

