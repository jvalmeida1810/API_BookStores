from django.urls import path
from editorial import views

urlpatterns = [ 
    path('editorial/', views.EditorialView.as_view(), name="Editoria"),
    path('editorial/<int:pk>/', views.EditorialRetriveUpdateDestroyDetail.as_view(), name="Editoria"),
    
]