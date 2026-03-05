from django.db import models

# Create your models here.
class Lenovo(models.Model):
    title = models.CharField()
    series_number = models.IntegerField()
    