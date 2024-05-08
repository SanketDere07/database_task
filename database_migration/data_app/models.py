from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)

class Address(models.Model):
    email_address = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
