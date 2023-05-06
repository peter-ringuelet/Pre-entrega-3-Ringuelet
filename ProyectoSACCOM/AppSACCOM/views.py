from django.shortcuts import render
from django.http import HttpResponse
from AppSACCOM.models import *
from AppSACCOM.forms import *

# Create your views here.
def inicio(request):
    return render(request, "AppSACCOM/inicio.html")

def comision_directiva(request):
    return render(request, "AppSACCOM/comision.html")

def socios(request):
    return render(request, "AppSACCOM/socios.html")

def actividades(request):
    return render(request, "AppSACCOM/actividades.html")


def actividadFormulario(request):
 
      if request.method == "POST":
 
            miFormulario = ActividadFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  actividad = Actividad(nombre=informacion["nombre"], fecha_inicio=informacion["fecha_inicio"])
                  actividad.save()
                  return render(request, "AppSACCOM/inicio.html")
      else:
            miFormulario = ActividadFormulario()
 
      return render(request, "AppSACCOM/actividadFormulario.html", {"miFormulario": miFormulario})


def comisionFormulario(request):
 
      if request.method == "POST":
 
            miFormulario = ComisionFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  comision = ComisionDirectiva(nombre=informacion["nombre"], apellido=informacion["apellido"], dni=informacion["dni"], cargo=informacion["cargo"])
                  comision.save()
                  return render(request, "AppSACCOM/inicio.html")
      else:
            miFormulario = ComisionFormulario()
 
      return render(request, "AppSACCOM/comisionFormulario.html", {"miFormulario": miFormulario})


def socioFormulario(request):
 
      if request.method == "POST":
 
            miFormulario = SocioFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  socio = Socio(nombre=informacion["nombre"], apellido=informacion["apellido"], dni=informacion["dni"])
                  socio.save()
                  return render(request, "AppSACCOM/inicio.html")
      else:
            miFormulario = SocioFormulario()
 
      return render(request, "AppSACCOM/socioFormulario.html", {"miFormulario": miFormulario})


def busquedaActividad(request):
      return render(request, "AppSACCOM/busquedaActividad.html")

def buscar(request):
      if request.GET['nombre']:
            nombre = request.GET['nombre']
            actividades = Actividad.objects.filter(nombre__icontains=nombre)
            return render(request, "AppSACCOM/resultadosBusqueda.html", {"actividades": actividades, "nombre":nombre})
      else:
            respuesta = "No existen datos"
      
      return HttpResponse(respuesta)

