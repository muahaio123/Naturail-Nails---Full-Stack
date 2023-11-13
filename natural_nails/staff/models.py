from django.db import models

# Create your models here.
class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    cashToCheckRatio = models.FloatField(default=0.40)
    bu = models.IntegerField(default=0)
    phone = models.CharField(max_length=10, null=True)
