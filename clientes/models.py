from django.db import models
from django.urls import reverse

class Cliente(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    nit_cc = models.CharField(max_length=20)
    email = models.EmailField()
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    pago = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('cliente_detail', args=[self.codigo])