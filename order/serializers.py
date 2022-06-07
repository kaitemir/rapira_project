from rest_framework import serializers
from .models import Order




class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        total_sum = 0
        request = self.context.get('request')
        user = request.user
        validated_data['user'] = user
        validated_data['status'] = 'new'
        validated_data['total_sum'] = 0
        products = validated_data.pop('products')
        order = Order.objects.create(**validated_data)
        for prod in products:
            total_sum += prod['product'].price * prod['quantity']
            Order.objects.create(order=order, **prod)
        order.total_sum = total_sum
        order.save()
        return order