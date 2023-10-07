from django.shortcuts import render
from .models import Animale, Colaboradore, Protectora

# Create your views here.
def blogs(request):
    return render(request, 'blog/blogs.html', {'blogs':['Animales','Protectoras','Colaboradores']})

def animale(request):
    animal=Animale.objects.all()
    return render(request, 'blog/animale.html', {'animal_mostrar':animal})

def protectora(request):
    protectora=Protectora.objects.all()
    return render(request, 'blog/protectora.html', {'protectora_mostrar':protectora})

def colaboradore(request):
    colaborador=Colaboradore.objects.all()
    return render(request, 'blog/colaboradore.html', {'colaborador_mostrar':colaborador})