from django.db import models
from inmuebles.models import Inmueble
from clientes.models import Cliente

class Recibo(models.Model):
    fecha = models.DateField()
    descripcion = models.CharField(max_length=100)
    abonos = models.DecimalField(max_digits=10, decimal_places=2)
    descuentos = models.DecimalField(max_digits=10, decimal_places=2)
    saldos = models.DecimalField(max_digits=10, decimal_places=2)
    inmueble = models.ForeignKey(Inmueble, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion
