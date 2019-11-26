from django.db import models

from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
#class User_Bank_ID(models.Model):
 #   customer_id = models.AutoField(primary_key = True)
  #  user = models.ForeignKey(User, on_delete = models.CASCADE)
    #created_on = models.DateTimeField(auto_now = True, blank = True)

#@receiver(post_save, sender = User)
#def create_user_bank_id(sender, instance, created, **kwargs):
 #   if created:
  #      User_Bank_ID.objects.create(user=instance)

#@receiver(post_save, sender = User)
#def save_user_bank_id(sender, instance, **kwargs):
    #instance.user_bank_id.save()


class Users_bank(models.Model):
    customer_id = models.AutoField(primary_key = True)  
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   # username = models.CharField(max_length = 20, blank = True)
   # username = models.ForeignKey('auth_user', on_delete=models.CASCADE)
   # username = models.CharField(unique = True, max_length = 50)
    password = models.CharField(max_length = 20, blank = True)
    created_on = models.DateTimeField(auto_now = True, blank = True)

@receiver(post_save, sender = User)
def create_bank_customerID(sender, instance, created, **kwargs):
   if created:
       Users_bank.objects.create(username = instance)

class Users(models.Model):
    customer_id = models.AutoField(primary_key = True)  
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    password = models.CharField(max_length = 20, blank = True)
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

class Customers_List(models.Model):
    #customer_id = models.IntegerField(primary_key = True)
    customer_id = models.ForeignKey(Users_bank, on_delete=models.CASCADE)
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
    customer_id = models.ForeignKey(Customers_List, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=50, null = False)
    account_balance = models.DecimalField(max_digits=13, decimal_places = 2, default = 0.00)

class checkingAcct(models.Model):
    transaction_id = models.AutoField(primary_key = True)
    customer_id = models.ForeignKey(Customers_List, on_delete=models.CASCADE)
    account_number = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=13, decimal_places = 2, null = True)
    vendor_name = models.CharField(max_length = 50)
    transaction_date = models.DateField(null = True)
    type_category = models.CharField(max_length = 100, null = True, default = 'unknown')
    transaction_type = models.CharField(max_length = 100, null = True, default = 'debit')
    


        
    
#@receiver(post_save, sender = Users_bank)
#def create_checking_account(sender, created, **kwargs):
   # if created:
     #   Accounts.objects.create(account_type='checking')
