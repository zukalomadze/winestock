from django.db import models


# Create your models here.
class Wine(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    year = models.PositiveSmallIntegerField(verbose_name='Year')
    alcohol = models.FloatField(verbose_name="Alcohol Level")
    stock = models.IntegerField(verbose_name="Stock")
    price = models.DecimalField(verbose_name="price", decimal_places=2, max_digits=6)

    def __str__(self):
        return self.name