from rest_framework import routers
from django.urls import path, include
from . import views

routers = routers.DefaultRouter()
routers.register(r'purchase', views.PurchaseViewSet)


urlpatterns = [
    path('category/', views.CategoryView.as_view(), name="Categoria"),
    path('category/<int:pk>/', views.CategoryRetriveUpdateDestroyDetail.as_view(), name="Categoria"),
   
    path('books/', views.BooksView.as_view(), name="Livro"),
    path('books/<int:pk>/', views.BooksRetriveUpdateDestroyDetail.as_view(), name="Livro"),
    
    path('', include(routers.urls)),
    path('purchase/<int:pk>/', views.PurchaseRetriveDestroyDetail.as_view(), name="Compra"),
    
    path('purchaseItems/', views.PurchaseItemsView.as_view(), name="Compra_Itens"),
    path('purchaseItems/<int:pk>/', views.PurchaseItemsRetriveUpdateDestroyDetail.as_view(), name="Compra_Itens"),
       
    
]