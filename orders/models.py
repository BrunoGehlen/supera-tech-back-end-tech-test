from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


# Create your models here.
class Orders(models.Model):
    owner = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE, blank=False)


class PurchasedProduct(models.Model):
    name = models.CharField(max_length=70)
    price = models.FloatField()
    score = models.IntegerField()

    sold_on_order = models.ForeignKey(Orders, related_name='products', on_delete=models.CASCADE, blank=False)
    
    def __str__(self):
        return self.name

