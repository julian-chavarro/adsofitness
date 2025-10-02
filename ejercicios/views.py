from django.shortcuts import render, redirect, get_object_or_404
from .models import Ejercicio
from .forms import EjercicioForm

def lista_ejercicios(request):
    ejercicios = Ejercicio.objects.all()
    return render(request, 'ejercicios/lista.html', {'ejercicios': ejercicios})

def crear_ejercicio(request):
    if request.method == 'POST':
        form = EjercicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ejercicios')
    else:
        form = EjercicioForm()
    return render(request, 'ejercicios/form.html', {'form': form})

def editar_ejercicio(request, id):
    ejercicio = get_object_or_404(Ejercicio, id=id)
    if request.method == 'POST':
        form = EjercicioForm(request.POST, instance=ejercicio)
        if form.is_valid():
            form.save()
            return redirect('lista_ejercicios')
    else:
        form = EjercicioForm(instance=ejercicio)
    return render(request, 'ejercicios/form.html', {'form': form})

def eliminar_ejercicio(request, id):
    ejercicio = get_object_or_404(Ejercicio, id=id)
    if request.method == 'POST':
        ejercicio.delete()
        return redirect('lista_ejercicios')
    return render(request, 'ejercicios/eliminar.html', {'ejercicio': ejercicio})
