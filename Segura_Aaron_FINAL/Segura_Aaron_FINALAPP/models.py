from django.db import models
from django.core.exceptions import ValidationError

# Modelo para Instituciones
class Institucion(models.Model):
    nombre = models.CharField(max_length=80, unique=True, verbose_name="Nombre de la Institución")
    direccion = models.CharField(max_length=255, blank=True, null=True, verbose_name="Dirección")
    telefono = models.CharField(max_length=15, blank=True, null=True, verbose_name="Teléfono")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Institución"
        verbose_name_plural = "Instituciones"

# Modelo para Inscritos
class Inscrito(models.Model):
    ESTADO_CHOICES = [
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO_ASISTEN', 'No Asisten'),
    ]

    nombre = models.CharField(max_length=100, verbose_name="Nombre Completo")
    email = models.EmailField(verbose_name="Correo Electrónico")
    telefono = models.CharField(max_length=15, verbose_name="Teléfono")
    nro_personas = models.PositiveIntegerField(verbose_name="Número de Personas")
    fecha_inscripcion = models.DateField(auto_now_add=True, verbose_name="Fecha de Inscripción")
    hora_inscripcion = models.TimeField(auto_now_add=True, verbose_name="Hora de Inscripción")
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE, verbose_name="Institución")
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='RESERVADO', verbose_name="Estado")
    observacion = models.TextField(blank=True, null=True, verbose_name="Observaciones")

    def clean(self):
        super().clean()
        
        # Validar número de personas
        if self.nro_personas is None:
            raise ValidationError("El número de personas es obligatorio.")
        if not (1 <= self.nro_personas <= 30):
            raise ValidationError("El número de personas debe estar entre 1 y 30 maximo.")
        
        # Validar nombre de la institución
        if self.institucion and len(self.institucion.nombre) > 80:
            raise ValidationError("El nombre de la institución no puede superar los 80 caracteres.")

    def __str__(self):
        return f"{self.nombre} - {self.institucion.nombre} ({self.estado})"

    class Meta:
        verbose_name = "Inscrito"
        verbose_name_plural = "Inscritos"