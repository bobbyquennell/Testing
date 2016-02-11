from __future__ import unicode_literals

from django.db import models

class Role(models.Model):
    role_name = models.CharField(max_length=50)

class UserInfo(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    gender = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    role = models.ForeignKey(Role)

class Group(models.Model):
    group_name = models.CharField(max_length=50)
    user = models.ManyToManyField(UserInfo)


class Asset(models.Model):
    host_name = models.CharField(max_length=256)
    ip_address = models.GenericIPAddressField()
    user_group = models.ForeignKey(Group)



