from django.db import models


# Create your models here.

class Feedback(models.Model):
    objects = models.Manager()
    content = models.CharField(max_length=2000)
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    subject = models.CharField(max_length=100)
