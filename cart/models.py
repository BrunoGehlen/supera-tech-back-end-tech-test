from rest_framework.authentication import TokenAuthentication
from django.db import models
from django.db import models
from products.models import Product
from django.contrib.auth import get_user_model


User = get_user_model()


# Create your models here.
class Cart(models.Model):
    products = models.ManyToManyField(Product, blank=True)
    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
