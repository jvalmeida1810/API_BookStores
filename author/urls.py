from django.urls import path
from author import views

urlpatterns = [
    path('author/', views.AuthorView.as_view(), name="Autor"),
    path('author/<int:pk>/', views.AuthorRetriveUpdateDestroyDetail.as_view(), name="Autor"),
    
]