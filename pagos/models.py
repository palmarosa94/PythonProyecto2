from django.db import models
from django.conf import settings

class Pagos(models.Model):
    nro_siniestro = models.CharField(max_length=30, verbose_name="Número de siniestro")
    nro_factura = models.CharField(
        max_length=15,
        null=True, blank=True, 
        verbose_name="Número de factura",
        help_text="Formato: 000-0000000000"
    )
    fecha_factura = models.DateField(null=True, blank=True, verbose_name="Fecha de emisión de la factura")
    importe = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Importe"
    )
    fecha_solicitud = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de solicitud")
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='pagos',
        verbose_name="Usuario"
    )

    def __str__(self):
        return f"Siniestro {self.nro_siniestro} - Factura {self.nro_factura} - ${self.importe}"

    