from django.db import models


class Address(models.Model):
    name = models.CharField(max_length=200)
    addr = models.TextField()
    rdate = models.DateTimeField(auto_now=True)
    # rdate = models.DateTimeField(auto_now=True)

    # mysql 예시
    # create table address (
    #   id int not null primary key autoincrement,
    #   name varchar
    #   addr text not null,
    #   rdate date not null
    # )


class Board(models.Model):
    writer = models.CharField(max_length=15)
    email = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    content = models.TextField()
    rdate = models.DateTimeField(auto_now=True)


# 패스워드는 세션에 포함x
# https://docs.djangoproject.com/en/4.0/ref/models/fields/
class Member(models.Model):
    # null default = False
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50, unique=True)
    pwd = models.CharField(max_length=30)
    phone = models.CharField(max_length=50)
    rdate = models.DateTimeField(auto_now=True)
    udate = models.DateTimeField(auto_now=True)


