from rest_framework import serializers
from shop.models import Product
from shop.serializers import ProductSerializer
from .models import Order,OrderItem
from .cart import Cart
from .tasks import order_created

class CartItemSerializer(serializers.Serializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    quantity = serializers.IntegerField(min_value=1)
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['product'] = ProductSerializer(instance['product']).data
        return data

class OrderItemSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    
    class Meta:
        model = OrderItem
        fields = '__all__'
        extra_kwargs = {
            'order':{'write_only':True},
        }
    
    def get_total_price(self, obj):
        return obj.get_cost()
    
    def to_representation(self, obj):
        data = super().to_representation(obj)
        data['product'] = ProductSerializer(obj.product).data
        return data

class OrderSerializer(serializers.ModelSerializer):
    order_items = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()
    
    class Meta:
        model = Order
        fields = '__all__'
    
    def get_order_items(self, instance):
        return OrderItemSerializer(instance.items, many=True).data
    
    def get_total_price(self, obj):
        return obj.get_total_cost()
    
    def create(self, validated_data):
        order = super().create(validated_data)
        cart = Cart(self.context.get('request'))
        for item in cart:
            order_item_serilzer = OrderItemSerializer(data={
                'order': order.id,
                'product': item['product']['id'],
                'quantity': item['quantity'],
                'price': item['price']
            })
            if order_item_serilzer.is_valid():
                order_item_serilzer.save()
        cart.clear()
        #send email order created using celery task
        order_created.delay(order.id)
        return order