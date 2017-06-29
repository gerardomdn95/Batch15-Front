from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'home/index.html')

def contacto(request):
    contacto = "Gerardo Medina"
    list_directions = ['Cerro del Perote #136 Colinas del Cimatario', 'Casa2']
    administradores = [
    {'nombre':"Luis", 'apellidos': "Salazar Torres", 'email': "makako@gmail.com", 'puesto': True},
    {'nombre':"Leidi", 'apellidos': "Gomez", 'email': "simio@gmail.com", 'encargado': False},
    {'nombre':"Fabioladora", 'apellidos': "Olvera", 'email': "fabz@gmail.com", 'encargado': True}
    ]

    return render(request, 'contacto.html',{'contacto1':contacto, 'direcciones':list_directions,
    'admins': administradores})

def agregar(request):
    return render(request,'home/agregar.html')