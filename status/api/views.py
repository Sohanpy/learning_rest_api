from rest_framework import viewsets
from status.models import Status
from .serializer import ListSerializers

class ListView(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = ListSerializers