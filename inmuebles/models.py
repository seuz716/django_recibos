from django.db import models
from clientes.models import Cliente
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

class Inmueble(models.Model):
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    num_habitaciones = models.PositiveIntegerField()
    num_banos = models.PositiveIntegerField()
    servicios_publicos = models.BooleanField(default=True)
    calificacion = models.DecimalField(max_digits=3, decimal_places=1)
    habitabilidad = models.CharField(max_length=100)
    propietario = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    foto_principal = models.ImageField(upload_to='inmuebles/')
    foto_thumbnail = ImageSpecField(source='foto_principal', processors=[ResizeToFit(200, 200)], format='JPEG', options={'quality': 90})

    def __str__(self):
        return self.direccion

