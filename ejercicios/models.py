from django.db import models

class Ejercicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=50)  # fuerza, cardio, movilidad, etc.
    nivel = models.CharField(max_length=20, choices=[
        ('principiante', 'Principiante'),
        ('intermedio', 'Intermedio'),
        ('avanzado', 'Avanzado'),
    ])
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
