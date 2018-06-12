from django.db import models

# Create your models here.

class Sample(models.Model):

    name = models.CharField(unique=True, default="", max_length=100)
    comment = models.CharField(null=True, default="", max_length=100)

