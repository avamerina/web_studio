from rest_framework import serializers

from orders.models import Order, File


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ['slug']

    def create(self, validated_data):
        return super().create(validated_data)


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = '__all__'
