from django.urls import path
from AppSACCOM import views

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('comision', views.comision, name='Comision'),
    path('socio', views.socio, name="Socios"),
    path('actividad', views.actividad, name="Actividades"),
    path('buscar/', views.buscar),
    path('actividad/list', views.ActividadList.as_view(), name='ActividadList'),
    path('actividad/(?P<pk>\d+)$', views.ActividadDetalle.as_view(), name='ActividadDetail'),
    path('actividad/nuevo/', views.ActividadCreacion.as_view(), name='ActividadNew'),
    path('actividad/editar/(?P<pk>\d+)$', views.ActividadUpdate.as_view(), name='ActividadEdit'),
    path('actividad/borrar/(?P<pk>\d+)$', views.ActividadDelete.as_view(), name='ActividadDelete'),
    path('socio/list', views.SocioList.as_view(), name='SocioList'),
    path('socio/(?P<pk>\d+)$', views.SocioDetalle.as_view(), name='SocioDetail'),
    path('socio/nuevo/', views.SocioCreacion.as_view(), name='SocioNew'),
    path('socio/editar/(?P<pk>\d+)$', views.SocioUpdate.as_view(), name='SocioEdit'),
    path('socio/borrar/(?P<pk>\d+)$', views.SocioDelete.as_view(), name='SocioDelete'),
    path('comision/list', views.ComisionList.as_view(), name='ComisionList'),
    path('comision/(?P<pk>\d+)$', views.ComisionDetalle.as_view(), name='ComisionDetail'),
    path('comision/nuevo/', views.ComisionCreacion.as_view(), name='ComisionNew'),
    path('comision/editar/(?P<pk>\d+)$', views.ComisionUpdate.as_view(), name='ComisionEdit'),
    path('comision/borrar/(?P<pk>\d+)$', views.ComisionDelete.as_view(), name='ComisionDelete'),
]
