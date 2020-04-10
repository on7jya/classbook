from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404, redirect
from .forms import DepartamentForm
from .models import Departament


def departament_list(request):
    departaments = Departament.objects.all().order_by('id')
    context = {'departaments': departaments, }
    return render(request, 'departament/departament_list.html', context)


def departament_add(request):
    if request.method == "POST":
        form = DepartamentForm(request.POST)
        if form.is_valid():
            departament = form.save(commit=False)
            departament.name = form.cleaned_data['name']
            departament.save()
            return redirect('departament-list')
    else:
        form = DepartamentForm()
    return render(request, 'departament/departament_add.html',
                  {'form': form})


def departament_edit(request, departament_id):
    departament = get_object_or_404(Departament, pk=departament_id)
    if request.method == "POST":
        form = DepartamentForm(request.POST, instance=departament)
        if form.is_valid():
            departament = form.save(commit=False)
            departament.name = form.cleaned_data['name']
            departament.save()
            return redirect('departament-list')
    else:
        form = DepartamentForm(instance=departament)
    return render(request, 'departament/departament_edit.html',
                  {'form': form})


def departament_delete(request, departament_id):
    departament = get_object_or_404(Departament, pk=departament_id)

    try:
        departament.delete()
    except ProtectedError:
        messages.warning(request, 'Departament has related objects and can not be deleted')

    return redirect('departament-list')
