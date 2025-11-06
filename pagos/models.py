from django.db import models


class Pagos(models.Model):
    importe = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    nro_siniestro = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nro_siniestro} - {self.importe}"
    