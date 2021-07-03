from django.db import models

# Create your models here.
class PhoneModel(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True, db_index=True)
    ram = models.IntegerField()
    storage = models.IntegerField()
    price = models.IntegerField()
    stock = models.IntegerField(default=0)