import os
import django
import random
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from biblioteca.models import Autor, Libro, Resena

fake = Faker('es_ES')

def crear_autores(n=5):
    for _ in range(n):
        nombre = fake.name()
        Autor.objects.create(nombre=nombre)

def crear_libros(n=10):
    autores = list(Autor.objects.all())
    for _ in range(n):
        titulo = fake.sentence(nb_words=4)
        resumen = fake.paragraph(nb_sentences=10)
        autor = random.choice(autores)
        Libro.objects.create(titulo=titulo, resumen=resumen, autor=autor)

def crear_resenas(n=30):
    libros = list(Libro.objects.all())
    for _ in range(n):
        libro = random.choice(libros)
        texto = fake.paragraph(nb_sentences=5)
        calificacion = random.randint(1, 5)
        Resena.objects.create(libro=libro, texto=texto, calificacion=calificacion)

if __name__ == '__main__':
    crear_autores()
    crear_libros()
    crear_resenas()
    print("✅ Datos de prueba generados correctamente.")
