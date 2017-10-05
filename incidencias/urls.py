from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^incidencia/(?P<pk>\d+)/$', views.UpdateViewIncidencia.as_view(), name="UpdateViewIncidencia"),
	url(r'^incidencias/(?P<pk>\d+)/$', views.CRViewIncidencias.as_view(), name="CRViewIncidencias"),

]