from rest_framework import serializers

from logistic.models import Product, StockProduct, Stock


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Product
        fields = '__all__'


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['address', 'positions']

    def create(self, validated_data):
        positions = validated_data.pop('positions')

        stock = super().create(validated_data)

        for position in positions:
            StockProduct.objects.create(product=position['product'],
                                        quantity=position['quantity'],
                                        price=position['price'],
                                        stock_id=stock.id)

        return stock

    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')

        stock = super().update(instance, validated_data)

        # для варианта с очисткой списка продуктов склада
        # StockProduct.objects.filter(stock_id=stock.id).delete()

        for position in positions:
            StockProduct.objects.update_or_create(product=position['product'],
                                                  quantity=position['quantity'],
                                                  price=position['price'],
                                                  stock_id=stock.id)

        return stock
