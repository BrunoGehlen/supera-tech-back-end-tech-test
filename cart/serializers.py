from .models import Cart
from products.models import Product
from rest_framework import serializers


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ('url', 'cart_costs', 'products')

    products = ProductSerializer(many=True)

    cart_costs = serializers.SerializerMethodField()

    def get_cart_costs(self, obj):
        products = obj.products.all()
        
        products_cost = sum([product.price for product in products])
        delivery_cost = (len(products) * 10) if products_cost < 250 else 0
        
        return {
            'sub_total': products_cost,
            'total': delivery_cost + products_cost,
            'delivery_cost': delivery_cost,
        }
        
class CheckoutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ('url', 'cart_costs')

    cart_costs = serializers.SerializerMethodField()

    def get_cart_costs(self, obj):
        products = obj.products.all()
        
        products_cost = sum([product.price for product in products])
        delivery_cost = (len(products) * 10) if products_cost < 250 else 0
        
        return {
            'sub_total': products_cost,
            'total': delivery_cost + products_cost,
            'delivery_cost': delivery_cost,
        }
        