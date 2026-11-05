from django.db import models

class Equipo(models.Model):
    ESTADO_CHOICES = [
        ('Disponible', 'Disponible'),
        ('Prestado', 'Prestado'),
    ]

    serial = models.CharField(max_length=50, unique=True)
    tipo = models.CharField(max_length=50)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Disponible')

    def __str__(self):
        return f"{self.tipo} ({self.serial}) - {self.estado}"

class Prestamo(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='prestamos')
    documento_aprendiz = models.CharField(max_length=20)
    ambiente = models.CharField(max_length=50)
    fecha_prestamo = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Préstamo de {self.equipo.serial} a {self.documento_aprendiz}"