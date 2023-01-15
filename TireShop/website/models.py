from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)
    balance = models.IntegerField(default=0)
    def last_address(self):
        return CustomerHasCart.objects.filter(customer_id=self.id).latest('address')

class Cart(models.Model):
    adress = models.CharField(max_length=100)

class CustomerHasCart(models.Model):
    customer_id = models.IntegerField()
    cart_id = models.IntegerField()

