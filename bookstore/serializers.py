from rest_framework import serializers
from .models import Category, Books, Purchase, PurchaseItems


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'


class PurchaseItemsSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()

    class Meta:
        model = PurchaseItems
        fields = ('books', 'quantity', 'total')
        depth = 2

    def get_total(self, obj):
        return obj.quantity * obj.books.price


class PurchaseSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    items = PurchaseItemsSerializer(many=True)

    class Meta:
        model = Purchase
        fields = ('id', 'status', 'user', 'items', 'total')

    def get_status(self, obj):

        status_mapping = {
            1: 'CARRINHO',
            2: 'REALIZADO',
            3: 'PAGO',
            4: 'Entregue'
        }
        return status_mapping.get(obj.status, 'Desconhecido')


class CreateEditPurchaseItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseItems
        fields = ('books', 'quantity')


class CreateEditPurchaseSerializer(serializers.ModelSerializer):
    items = CreateEditPurchaseItemsSerializer(many=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Purchase
        fields = ('id', 'user', 'items')

    def create(self, validated_data):
        items = validated_data.pop('items')
        purchase = Purchase.objects.create(**validated_data)
        for item in items:
            PurchaseItems.objects.create(purchase=purchase, **item)
        purchase.save()
        return purchase

    def update(self, instance, validated_data):
        items = validated_data.pop('items')
        if items:
            instance.items.all().delete()
            for item in items:
                PurchaseItems.objects.create(purchase=instance, **item)
            instance.save()
            return instance
