from rest_framework import serializers
from .models import Category,Product

class CategorySerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    
    class Meta:
        model=Category
        fields='__all__'
    
    def get_url(self,obj):
        return obj.get_absolute_url()

class ProductSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    
    class Meta:
        model=Product
        fields='__all__'
        extra_kwargs={
            'image':{'required':False},
        }
    
    def get_url(self, obj):
        return obj.get_absolute_url()
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['category'] = CategorySerializer(instance.category).data
        return data