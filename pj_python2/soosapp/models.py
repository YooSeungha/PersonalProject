from django.db import models

class Address(models.Model):
    name = models.CharField(max_length=200)
    addr = models.TextField()
    rdate = models.DateTimeField()

class Board(models.Model):
    writer = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    rdate = models.DateTimeField()

class Member(models.Model):
    name = models.CharField(max_length=30)
    email = models.TextField(primary_key=True)
    pwd = models.CharField(max_length=30)
    phone = models.CharField(max_length=50)
    rdate = models.DateTimeField()
    udate = models.DateTimeField()

