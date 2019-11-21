from django.db import models

from django.conf import settings

# Create your models here.


class Users(models.Model):
    customer_id = models.AutoField(primary_key = True)
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   # username = models.CharField(unique = True, max_length = 50)
    password = models.CharField(max_length = 20)
    created_on = models.DateTimeField(auto_now = True, blank = True)

class Customers(models.Model):
    customer_id = models.IntegerField(primary_key = True)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    middle_name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    state = models.CharField(max_length = 20)
    zipcode = models.IntegerField(blank = True, null = True)
    phone_number = models.CharField(max_length = 12, blank = True, null = True)

class Accounts(models.Model):
    account_number = models.AutoField(primary_key = True)
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=50, null = False)
    account_balance = models.DecimalField(max_digits=13, decimal_places = 2, default = 0.00)

class checkingAcct(models.Model):
    transaction_id = models.AutoField(primary_key = True)
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    account_number = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=13, decimal_places = 2, null = True)
    vendor_name = models.CharField(max_length = 50)
    transaction_date = models.DateField(null = True)
    type_category = models.CharField(max_length = 100, null = True, default = 'unknown')



    
    