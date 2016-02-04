from __future__ import unicode_literals

from django.db import models

class Role(models.Model):
    role_name = models.CharField(max_length=50)

class Group(models.Model):
    group_name = models.CharField(max_length=50)

class UserInfo(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    gender = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    role_id = models.ForeignKey(Role)
    group_relation = models.ManyToManyField(Group)





