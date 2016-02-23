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
    host_name = models.CharField(max_length=256,unique=True)
    ip_address = models.GenericIPAddressField(unique=True)   #support both ipv4 and ipv6
    # IPAddressField only supports IPV4
    port = models.IntegerField(default=22)
    system_type_choices = (

        ('linux',"LINUX"),
        ('win32',"WINDOWS")

    )
    system_type = models.CharField(choices=system_type_choices,max_length=32)
    enabled = models.BooleanField(default=True)
    create_date = models.DateTimeField()
    online_date = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(Group)  #group is actually an Class Group's object.
    def __unicode__(self):
        return self.host_name






