from rest_framework import viewsets
from .models import Autor, Libro, Resena
from .serializers import AutorSerializer, LibroSerializer, ResenaSerializer
from django.http import HttpResponse

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

class ResenaViewSet(viewsets.ModelViewSet):
    queryset = Resena.objects.all()
    serializer_class = ResenaSerializer

    from django.http import HttpResponse

def home(request):
    return HttpResponse("📚 Bienvenido a la API de la Biblioteca")
