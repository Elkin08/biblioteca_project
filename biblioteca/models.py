from django.db import models
from django.core.exceptions import ValidationError

# Validadores personalizados
def validar_nombre(valor):
    if not valor.strip():
        raise ValidationError("El nombre no puede estar vacío o solo contener espacios.")

def validar_resumen(resumen):
    if len(resumen.strip()) < 30:
        raise ValidationError("El resumen debe tener al menos 30 caracteres.")

def validar_calificacion(valor):
    if valor < 1 or valor > 5:
        raise ValidationError("La calificación debe estar entre 1 y 5.")

class Autor(models.Model):
    nombre = models.CharField(max_length=100, validators=[validar_nombre])

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="libros")
    resumen = models.TextField(validators=[validar_resumen])

    def __str__(self):
        return self.titulo

class Resena(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name="resenas")
    texto = models.TextField()
    calificacion = models.IntegerField(validators=[validar_calificacion])

    def __str__(self):
        return f"{self.libro.titulo} - {self.calificacion} estrellas"
