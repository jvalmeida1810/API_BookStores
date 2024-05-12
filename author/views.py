from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from app.permissions import GlobalDefaultPermission
from .models import Author
from .serializers import AuthorSerializer

class AuthorView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, GlobalDefaultPermission,)
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorRetriveUpdateDestroyDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, GlobalDefaultPermission,)
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
