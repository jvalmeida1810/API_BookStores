from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('bookstore.urls')),
    path('api/v1/', include('author.urls')),
    path('api/v1/', include('editorial.urls')),
    path('api/v1/', include('authentication.urls')),
    path('api/v1/', include('spectacular.urls')),
    
    
]