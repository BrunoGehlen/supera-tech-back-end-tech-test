from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=70)
    price = models.FloatField()
    score = models.IntegerField()
    image = models.CharField(max_length=250)

    def __str__(self):
        return self.name