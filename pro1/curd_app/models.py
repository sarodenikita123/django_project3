from django.db import models


class Registration(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.IntegerField()
    birthday = models.DateField()
    address1 = models.CharField(max_length=20)
    address2 = models.CharField(max_length=20)
    city = models.CharField(max_length=10)
    state = models.CharField(max_length=20)
    zip = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

