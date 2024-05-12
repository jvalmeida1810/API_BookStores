from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from app.permissions import GlobalDefaultPermission
from .models import Editorial
from .serializers import EditorialSerializer

class EditorialView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, GlobalDefaultPermission,)
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

class EditorialRetriveUpdateDestroyDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, GlobalDefaultPermission,)
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer
    