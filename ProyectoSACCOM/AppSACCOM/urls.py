from django.urls import path
from AppSACCOM import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('comision', views.comision, name='Comision'),
    path('socios', views.socio, name="Socios"),
    path('actividades', views.actividad, name="Actividades"),
    path('buscar/', views.buscar),
]
