from cart.models import Cart
from cart.serializers import CartSerializer
from cart.permissions import OwnedByUser
from products.models import Product
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action


class CartView(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [OwnedByUser]
    authentication_classes = [TokenAuthentication]

    @action(detail=False, methods=['post'])
    def add_product_to_cart(self, request, pk=None):
        cart = Cart.objects.get_or_create(owner=request.user)[0]
        Cart.objects.get(owner=request.user)
        product = Product.objects.get(id=request.data.pop("product_id"))
        cart.products.add(product)
        cart.save()
        serializer = CartSerializer(instance=cart, context={'request': request})
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    @action(detail=False, methods=['delete'])
    def remove_product_from_cart(self, request, pk=None):
        cart = Cart.objects.get_or_create(owner=request.user.id)[0]
        product = Product.objects.get(id=request.data.pop("product_id"))
        cart.products.remove(product)
        cart.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
