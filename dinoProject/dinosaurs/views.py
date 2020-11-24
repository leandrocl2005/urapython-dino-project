from rest_framework import viewsets
from .models import Dinosaur
from .serializer import DinosaurSerializer


class DinosaurViewSet(viewsets.ModelViewSet):
    queryset = Dinosaur.objects.all()
    serializer_class = DinosaurSerializer
