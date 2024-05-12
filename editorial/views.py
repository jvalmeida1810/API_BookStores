from rest_framework import generics
from .models import Editorial
from .serializers import EditorialSerializer

class EditorialView(generics.ListAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer

class EditorialRetriveUpdateDestroyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer
    