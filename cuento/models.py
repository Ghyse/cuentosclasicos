from django.db import models

# Create your models here.
class Cuento(models.Model):
	title = models.CharField(max_length=200)
	texto = models.TextField()

	def __str__(self):
		return self.title

class Capitulo(models.Model):
	cuento = models.ForeignKey(Cuento, related_name='cuentos' )
	texto = models.TextField()

	def __str__(self):
		return self.texto
