from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from biblioteca.views import AuthorViewSet, BookViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
router.register(r'reviews', ReviewViewSet)

def home(request):
    return HttpResponse("Bienvenido a la API de libros")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),          # Ruta raíz con mensaje simple
    path('api/', include(router.urls)),  # Rutas del API
]
