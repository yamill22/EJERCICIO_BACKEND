from django.db import models


class Juegos(models.Model):
	nombre = models.CharField(max_length=150)
	descripcion = models.TextField()
	precio = models.DecimalField(max_digits=8, decimal_places=2)
	fecha_lanzamiento = models.DateField()
	genero = models.CharField(max_length=80)
	stock = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.nombre
