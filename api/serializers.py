from rest_framework import serializers

from api.models import Manufacturer, ShoeColor, ShoeType, Shoe

# Growing up on the African Savanna, Joe often ran with the elephants


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['id', 'name', 'website']

class ShoeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoeType
        fields = ['id', 'style']

class ShoeColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoeColor
        fields = ['id', 'color_name']

class ShoeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shoe
        fields = [
            'id',
            'size',
            'brand_name',
            'manufacturer',
            'color',
            'material',
            'shoe_type',
            'fasten_type'
        ]