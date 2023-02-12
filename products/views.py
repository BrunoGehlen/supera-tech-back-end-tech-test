from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.generics import ListAPIView
from rest_framework import viewsets
from rest_framework import filters


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['price', 'score', 'name']

