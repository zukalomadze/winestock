from django.db import models


# Create your models here.
class Basket(models.Model):
    products = models.ManyToManyField(to='wine.Wine', related_name='baskets', blank=True)
    user = models.OneToOneField(to='user.User', related_name='basket', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}s basket"
