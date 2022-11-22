from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, loader, Context
from .models import Familia

# Create your views here.

def integrante(request):
    integrante1=Familia(nombre='Luciano', apellido= 'Pardo', edad=39, FechaNac="1983-09-02")
    integrante2=Familia(nombre='Guillermo', apellido='Pardo', edad=72, FechaNac="1950-11-06")
    integrante3=Familia(nombre='Silvia', apellido='Miguelez', edad=67, FechaNac="1955-01-12")
    integrante1.save()
    integrante2.save()
    integrante3.save()
    familia = f'Se guardaron los siguientes integrates: <br> ------------------------ <br> Nombre: {integrante1.nombre} <br> Apellido: {integrante1.apellido} <br> Edad: {str(integrante1.edad)} <br> FechaNac: {str(integrante1.FechaNac)} <br> ------------------------ <br> Nombre: {integrante2.nombre} <br> Apellido: {integrante2.apellido} <br> Edad: {str(integrante2.edad)} <br> FechaNac: {str(integrante2.FechaNac)} <br> ------------------------ <br> Nombre: {integrante3.nombre} <br> Apellido: {integrante3.apellido} <br> Edad: {str(integrante3.edad)} <br> FechaNac: {str(integrante3.FechaNac)} <br>'
    return HttpResponse (familia)

def inicio(self):
    fam="Pardo"
    dicionario={'family':fam}
    plantilla=loader.get_template('index.html')
    doc=plantilla.render(dicionario)
    return HttpResponse(doc)




