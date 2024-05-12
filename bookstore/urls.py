from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.CategoryView.as_view(), name="Categoria"),
    path('category/<int:pk>/', views.CategoryRetriveUpdateDestroyDetail.as_view(), name="Categoria"),
   
    path('books/', views.BooksView.as_view(), name="Livro"),
    path('books/<int:pk>/', views.BooksRetriveUpdateDestroyDetail.as_view(), name="Livro"),
    
    path('purchase/', views.PurchaseView.as_view(), name="Compra"),
    path('purchase/<int:pk>/', views.PurchaseRetriveUpdateDestroyDetail.as_view(), name="Compra"),
    
    path('purchaseItems/', views.PurchaseItemsView.as_view(), name="Compra_Itens"),
    path('purchaseItems/<int:pk>/', views.PurchaseItemsRetriveUpdateDestroyDetail.as_view(), name="Compra_Itens"),
       
    
]