from .models import Orders, PurchasedProduct
from rest_framework import serializers


class PurchasedProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PurchasedProduct
        fields = ['name', 'price', 'score']

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Orders
        fields = ['products', 'order_costs']

    products = PurchasedProductSerializer(many=True)
    order_costs = serializers.SerializerMethodField()

    def get_order_costs(self, obj):
        products = obj.products.all()
        
        products_cost = sum([product.price for product in products])
        delivery_cost = (len(products) * 10) if products_cost < 250 else 0
        
        return {
            'sub_total': products_cost,
            'total': delivery_cost + products_cost,
            'delivery_cost': delivery_cost,
        }
        