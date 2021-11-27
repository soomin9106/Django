from django.db import models
from django.db.models.base import Model

# Create your models here.

class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False)
