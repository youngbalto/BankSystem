from django.db import models
from datetime import date

# Create your models here.
# TODO write model fields and relationships
class AccountNumber(models.Model):
    number = models.CharField(max_length=20, null=False, primary_key=True)
    entry_date = models.DateField(default=date.today())
    account_balance = models.IntegerField(default=0, null=False)


class Credit(models.Model):
    sum = models.IntegerField(null=False,max_length=8)
    date_signed = models.DateField()
    date_due = models.DateField()


class Creditor(models.Model):
    name = models.CharField(null=False)
    account = models.OneToOneField(AccountNumber,models.CASCADE)
    credit = models.OneToManyField(Credit,models.CASCADE)


class Admin(models.Model):
    username = models.CharField(null=False)
    password = models.CharField(null=False)


class Client(models.Model):
    passportNumber = models.CharField(max_length=15, null=False)
    name = models.CharField(max_length=15, null=False)
    surname = models.CharField(max_length=15, null=False)
    client_number = models.OneToOneField(AccountNumber, on_delete=models.CASCADE, primary_key=True)


class Director(models.Model):
    name = models.CharField(max_length=30, null=False)
    email = models.CharField(max_length=12, null=False)
    phone = models.CharField(max_length=12, null=False)


class BookManager(models.Model):
    name = models.CharField(max_length=30, null=False)
    email = models.CharField(max_length=12, null=False)
    phone = models.CharField(max_length=12, null=False)
    is_main = models.BooleanField(default=False)
