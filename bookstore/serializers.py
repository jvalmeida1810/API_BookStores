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
        

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'
        
      

class PurchaseItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseItems
        fields = '__all__'
        
