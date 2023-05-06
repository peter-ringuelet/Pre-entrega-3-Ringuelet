from django.urls import path
from AppSACCOM import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('comision', views.comision, name='Comision'),
    path('socios', views.socio, name="Socios"),
    path('actividades', views.actividad, name="Actividades"),
    #path('actividadFormulario', views.actividadFormulario, name="ActividadFormulario"),
    #path('comisionFormulario', views.comisionFormulario, name="ComisionFormulario"),
    #path('socioFormulario', views.socioFormulario, name="SocioFormulario"),
    #path('busquedaActividad', views.busquedaActividad, name="BusquedaActividad"),
    path('buscar/', views.buscar),
]
