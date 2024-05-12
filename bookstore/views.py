from rest_framework import generics
from .models import Category, Books, Purchase, PurchaseItems
from .serializers import CategorySerializer, BooksSerializer, PurchaseSerializer, PurchaseItemsSerializer

class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetriveUpdateDestroyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    
class BooksView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

class BooksRetriveUpdateDestroyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    queryset.delete()
   
class PurchaseView(generics.ListAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

class PurchaseRetriveUpdateDestroyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

class PurchaseItemsView(generics.ListAPIView):
    queryset = PurchaseItems.objects.all()
    serializer_class = PurchaseItemsSerializer

class PurchaseItemsRetriveUpdateDestroyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseItems.objects.all()
    serializer_class = PurchaseItemsSerializer
    
    
 