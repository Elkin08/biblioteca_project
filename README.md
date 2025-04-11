# 📚 Biblioteca API

Este proyecto es una API REST desarrollada con Django y Django REST Framework para gestionar autores, libros y reseñas de una biblioteca.

## 🚀 Características

- CRUD completo para autores, libros y reseñas
- Validaciones personalizadas (resumen mínimo, calificación entre 1 y 5)
- Navegador de API (DRF)
- Panel de administración de Django
- Script para poblar datos de prueba con Faker
- Soporte para CORS en desarrollo

## 🧰 Tecnologías usadas

- Python 3.10+
- Django 5.x
- Django REST Framework
- Faker
- SQLite (por defecto)

## ⚙️ Instalación y ejecución local

```bash
# 1. Clona el repositorio
git clone https://github.com/Elkin08/biblioteca_project.git
cd biblioteca_project

# 2. Crea y activa entorno virtual
python -m venv env
env\Scripts\activate  # En Windows

# 3. Instala dependencias
pip install -r requirements.txt

# 4. Aplica migraciones
python manage.py makemigrations
python manage.py migrate

# 5. Crea superusuario
python manage.py createsuperuser

# 6. Ejecuta el servidor
python manage.py runserver
```
## 🌐 Navegación

- Bienvenida: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Navegador de API: [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)
- Panel admin: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

## 📸 Capturas de pantalla
Panel de Administración con datos:
![Imagen de WhatsApp 2025-04-10 a las 18 30 31_0836b449](https://github.com/user-attachments/assets/40e362a5-3c90-49c5-9c6b-c9ffcadbfd0d)

Ejecución del Script de Carga Inicial:
![image](https://github.com/user-attachments/assets/98e384af-b91e-43d9-a5e1-556d8b240922)

## 👤 Autor
Elkin Andres LM
📧 elkinandreslm@ufps.edu.co

## 📝 Licencia
Este proyecto está bajo la licencia MIT.


