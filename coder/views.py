from django.shortcuts import render, redirect, get_object_or_404
from coder.forms import *
from coder.models import Abogados, Peritos, Jurisdicciones
from django.db.models import Q
from django.contrib import messages
from .forms import AbogadosForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "coder/index.html")

def test(request):
    return render(request, "coder/test.html")

@login_required
def crear_abogado(request):
    if request.method == "POST":
        form = AbogadosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("abogados_list")
    else:
        form = AbogadosForm()
        
    return render(request, "coder/abogado_form.html", {'form': form})

def crear_perito(request):
    if request.method == "POST":
        form = PeritosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = PeritosForm()
        
    return render(request, "coder/perito_form.html", {'form': form})

def crear_jurisdicciones(request):
    if request.method == "POST":
        form = JurisdiccionesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = JurisdiccionesForm()
    
    return render(request, "coder/jurisdicciones_form.html", {'form': form})
            

def lista_abogados(request):
    query = request.GET.get('q', '').strip()
    if query:
        abogado = Abogados.objects.filter(
            Q(nombre__icontains=query) |
            Q(apellido__icontains=query) |
            Q(nro_abogado__icontains=query)
        ).order_by("nro_abogado")
    else:
        abogado = Abogados.objects.all().order_by("nro_abogado")
        
    return render(request, "coder/abogados_list.html", {"abogados": abogado, "query": query})

def eliminar_abogado(request, nro_abogado): 
    abogados = get_object_or_404(Abogados, nro_abogado=nro_abogado)
    abogados.delete()
    messages.success(request, "Abogado eliminado correctamente")
    return redirect("abogados_list")
    
def modificar_abogado(request, nro_abogado):
    abogados = get_object_or_404(Abogados, nro_abogado=nro_abogado)
    if request.method == 'POST':
        form = AbogadosForm(request.POST, instance=abogados)
        if form.is_valid():
            form.save()
            return redirect("abogados_list")
    else:
        form = AbogadosForm(instance=abogados)
        
    return render(request, "coder/abogado_form.html", {'form': form, 'edicion': True})


from django.shortcuts import render

def about(request):
    return render(request, "coder/about.html")

