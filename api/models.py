from django.db import models


class User(models.Model):
    u_name = models.CharField(max_length=32, unique=True)
    u_password = models.CharField(max_length=256)
    is_super = models.BooleanField(default=False)


class UserToken(models.Model):
    u_name = models.CharField(max_length=32, unique=True)
    u_token = models.CharField(max_length=256)


class Question(models.Model):
    title = models.CharField(max_length=256)
    u_name = models.CharField(max_length=32)
    context = models.CharField(max_length=65536)


class Answer(models.Model):
    qid = models.IntegerField(default=0)
    u_name = models.CharField(max_length=32)
    context = models.CharField(max_length=65536)
