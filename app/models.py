from django.db import models
from django.utils.timezone import *

# Create your models here.
# TODO write model fields and relationships


class AccountNumber(models.Model):
    number = models.CharField(max_length=20, null=False, primary_key=True)
    entry_date = models.DateField(default=now())
    account_balance = models.IntegerField(default=0, null=False)


class Client(models.Model):
    passportNumber = models.CharField(max_length=15, null=False,primary_key=True)
    name = models.CharField(max_length=15, null=False)
    password = models.CharField(max_length=18,null=False)
    surname = models.CharField(max_length=15, null=False)
    client_number = models.OneToOneField(AccountNumber, on_delete=models.CASCADE)


class BookManager(models.Model):
    name = models.CharField(max_length=30, null=False)
    email = models.CharField(max_length=12, null=False)
    password = models.CharField(max_length=18,null=False)
    phone = models.CharField(max_length=12, null=False)
    is_main = models.BooleanField(default=False)
    client = models.ForeignKey(Client,on_delete=models.CASCADE,default=None)


class Creditor(models.Model):
    name = models.CharField(null=False,max_length=20)
    account = models.OneToOneField(AccountNumber,models.CASCADE)


class Credit(models.Model):
    sum = models.IntegerField(null=False)
    date_signed = models.DateField()
    date_due = models.DateField()
    creditor = models.ForeignKey(Creditor,on_delete=models.CASCADE,default=None)


class Admin(models.Model):
    username = models.CharField(null=False,max_length=10)
    password = models.CharField(null=False,max_length=18)


class Director(models.Model):
    name = models.CharField(max_length=30, null=False)
    email = models.CharField(max_length=12, null=False)
    phone = models.CharField(max_length=12, null=False)
    book_manager = models.OneToOneField(BookManager,on_delete=models.CASCADE,default=None)

