from django.db import models

# Create your models here.
class book(models.Model):

    book = models.CharField(max_length = 20)
    