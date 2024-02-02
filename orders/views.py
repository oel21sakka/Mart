from rest_framework import viewsets,status
from rest_framework.response import Response
from .cart import Cart
from .serializers import CartItemSerializer

class CartViewSet(viewsets.ViewSet):
    
    def list(self, request):
        response = {}
        response['products'] = Cart(request).cart.values()
        response['total_price'] = Cart(request).get_total_price()
        response['total_quantity'] = len(Cart(request))
        return Response(response, status=status.HTTP_200_OK)
    
    def create(self, request):
        '''
        if method not post quantity is overwriten
        else quantity added to previous quantity
        '''
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            response = Cart(request).add(product = serializer.data['product'], quantity = int(serializer.data['quantity']),\
                override_quantity = request.method!='POST')
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request):
        '''
        If Product Provided just this product is deleted
        Else all products in the cart is deleted
        '''
        if 'product' in request.data:
            Cart(request).remove(request.data['product'])
        else:
            Cart(request).clear()
        return Response({'Message':'Done'}, status=status.HTTP_204_NO_CONTENT)