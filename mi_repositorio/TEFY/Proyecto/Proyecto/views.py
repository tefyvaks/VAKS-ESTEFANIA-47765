from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader

def saludo(request):
    return HttpResponse("Hola Django - Coder")

def segunda_vista(request):
    return HttpResponse("<br><br> Estefania Vaks")

def probandoTemplate(self):

    nom = "Estefania"
    ap = "Vaks"

    diccionario = {"nombre":nom, "apellido":ap}
    
    """miHtml = open("C:/Users/Lenovo/OneDrive/Escritorio/Tercer-Pre-Entrega-VAKS/Proyecto/Proyecto/Plantillas/template1.html")

    plantilla = Template(miHtml.read())

    miContexto = Context(diccionario)

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)"""

    plantilla = loader.get_template('template1.html')

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)

