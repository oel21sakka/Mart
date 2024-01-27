from rest_framework import generics
from .serializers import ProductSerializer,CategorySerializer
from .models import Product,Category


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class=CategorySerializer

class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class=ProductSerializer

class SingleCategoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class=CategorySerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

class SingleProductView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'