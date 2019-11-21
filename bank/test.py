# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Accounts(models.Model):
    account_number = models.AutoField(primary_key=True)
    customer = models.ForeignKey('Customers', models.DO_NOTHING, blank=True, null=True)
    account_type = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'accounts'


class Checkingacct(models.Model):
    customer = models.ForeignKey('Customers', models.DO_NOTHING, blank=True, null=True)
    account_number = models.IntegerField(blank=True, null=True)
    transaction_id = models.AutoField(primary_key=True)
    amount = models.DecimalField(max_digits=13, decimal_places=2, blank=True, null=True)
    type = models.CharField(max_length=50)
    vendor = models.CharField(max_length=50)
    transaction_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'checkingAcct'


class Customers(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.IntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers'


class Users(models.Model):
    customer_id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
