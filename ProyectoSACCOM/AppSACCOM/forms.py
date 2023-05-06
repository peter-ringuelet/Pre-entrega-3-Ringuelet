from django import forms 

class ActividadFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    fecha_inicio = forms.DateField()

class ComisionFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    dni = forms.IntegerField()
    cargo = forms.CharField(max_length=30)

class SocioFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    dni = forms.IntegerField()
