from django.contrib.auth.models import User
from django.db import models

class FacebookProfile(models.Model):
    user = models.ForeignKey(User)
    uid = models.CharField(max_length=50)
    link = models.URLField()
    gender = models.CharField(max_length=10, blank=True)
    