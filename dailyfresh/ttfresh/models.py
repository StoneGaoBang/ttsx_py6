from django.db import models


class UserInfo(models.Model):
    uname = models.CharField(max_length=40)
    upwd = models.CharField(max_length=40)

