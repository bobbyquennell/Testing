from __future__ import unicode_literals

from django.db import models

class Role(models.Model):
    role_name = models.CharField(max_length=50)

class UserInfo(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    role = models.ForeignKey(Role)


class Group(models.Model):
    group_name = models.CharField(max_length=50)
    user = models.ManyToManyField(UserInfo)


class Asset(models.Model):
    host_name = models.CharField(max_length=256)
    ip_address = models.GenericIPAddressField()
    group = models.ForeignKey(Group)  #group is actually an Class Group's object.
    def __unicode__(self):
        return self.host_name






