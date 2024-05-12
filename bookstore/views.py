from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Category, Books, Purchase, PurchaseItems
from .serializers import CategorySerializer, BooksSerializer, PurchaseSerializer, PurchaseItemsSerializer, CreateEditPurchaseSerializer
from app.permissions import GlobalDefaultPermission

class CategoryView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, GlobalDefaultPermission,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetriveUpdateDestroyDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, GlobalDefaultPermission,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    
class BooksView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, GlobalDefaultPermission,)
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

class BooksRetriveUpdateDestroyDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, GlobalDefaultPermission,)
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    
   
class PurchaseViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, GlobalDefaultPermission,)
    queryset = Purchase.objects.all()
    #serializer_class = PurchaseSerializer
    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return PurchaseSerializer
        return CreateEditPurchaseSerializer

class PurchaseRetriveDestroyDetail(generics.RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, GlobalDefaultPermission,)
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

class PurchaseItemsView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, GlobalDefaultPermission,)
    queryset = PurchaseItems.objects.all()
    serializer_class = PurchaseItemsSerializer

class PurchaseItemsRetriveUpdateDestroyDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, GlobalDefaultPermission,) 
    queryset = PurchaseItems.objects.all()
    serializer_class = PurchaseItemsSerializer
    
    
 