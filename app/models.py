from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class AtUser(models.Model):
    user = models.OneToOneField(User)
    userDept = models.CharField(max_length=20)
    userJob = models.CharField(max_length=20)
    userImage = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username


class Dept(models.Model):
    deptName = models.CharField(max_length=10)

    def __unicode__(self):
        return self.deptName


class AtSend(models.Model):
    sendType = models.CharField(max_length=20)
    sendText = models.TextField()
    sendTime = models.DateField(auto_now=True)
    sendDept = models.CharField(max_length=6)

    def __unicode__(self):
        return self.sendType
