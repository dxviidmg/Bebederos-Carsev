from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class VisitaDeAcuerdo(models.Model):
	escuela = models.OneToOneField(User)
	convenio_concertacion = models.FileField(upload_to='visita/concertaciones/%Y/%m/%d/', verbose_name="Convenio de concertación de aplicación de recurso")
	cedula_identificacion = models.FileField(upload_to='visita/identificaciones/%Y/%m/%d/', verbose_name="Cédula de identificación básica")
	acta_acuerdos = models.FileField(upload_to='visitas/actas/%Y/%m/%d/', verbose_name="Acta de acuerdos")
	croquis_modulo = models.FileField(upload_to='visitas/croquis/%Y/%m/%d/', verbose_name="Croquis de ubicación de modulo", default="default.pdf")	
	constancia_integracion_comite = models.FileField(upload_to='visitas/comites/%Y/%m/%d/', verbose_name="Constancia de Integración de Comité")
	plano_conjunto = models.FileField(upload_to='visitas/planosConjunto/%Y/%m/%d/', verbose_name="Plano de conjunto", null=True, blank=True)
	distribucion_planta = models.FileField(upload_to='visitas/distribuciones/%Y/%m/%d/', verbose_name="Distribución en planta", null=True, blank=True)	
	memoria_calculo = models.FileField(upload_to='instalaciones/memorias/%Y/%m/%d/', verbose_name="Memoria de cálculo hidrosanitario y eléctrico", null=True, blank=True)
	plano_instalacion_electrica = models.FileField(upload_to='visitas/pihs/%Y/%m/%d/', verbose_name="Plano de instalación electrica", null=True, blank=True)
	plano_instalacion_hidraulica = models.FileField(upload_to='visitas/pies/%Y/%m/%d/', verbose_name="Plano de instalación hidraulica con isométrico", null=True, blank=True)
	plano_instalacion_sanitaria = models.FileField(upload_to='visitas/piss/%Y/%m/%d/', verbose_name="Plano de instalación sanitaria  con isométrico", null=True, blank=True)
	creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")
	si = models.ForeignKey(User, related_name="si_visita_acuerdo")

	def __str__(self):
		return '{}'.format(self.escuela)

	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Visitas de acuerdo'

class InicioFuncionamiento(models.Model):
	escuela = models.OneToOneField(User)
	acta_funcionamiento = models.FileField(upload_to='funcionamiento/actas/%Y/%m/%d/', verbose_name="Acta de inicio de funcionamiento")
	video = models.FileField(upload_to='funcionamiento/videos/%Y/%m/%d/', verbose_name="Video de muestra del funcionamiento")
	creacion = models.DateTimeField(default=timezone.now, verbose_name="Fecha de creación")
	si = models.ForeignKey(User, related_name="si_entrega_bebedero", null=True, blank=True)

	def __str__(self):
		return '{}'.format(self.escuela)

	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Entregas de bebedero'

class ActaEntrega(models.Model):
	escuela = models.OneToOneField(User)
	acta_entrega = models.FileField(upload_to='entrega/actas/%Y/%m/%d/', verbose_name="Acta de entrega")
	si = models.ForeignKey(User, related_name="si_acta_entrega", null=True, blank=True, verbose_name="Superintendente")

	def __str__(self):
		return '{}'.format(self.escuela)

	class Meta:
		ordering = ['escuela']
		verbose_name_plural = 'Actas de entrega'		