from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import render, get_object_or_404, redirect
from .forms import SectionForm
from .models import Section


def section_list(request):
    sections = Section.objects.all().order_by('id')
    return render(request, 'section/section_list.html',
                  {'sections': sections})


def section_add(request):
    if request.method == "POST":
        form = SectionForm(request.POST)
        if form.is_valid():
            section = form.save(commit=False)
            section.name = form.cleaned_data['name']
            section.departament = form.cleaned_data['departament']
            section.save()
            print(form.cleaned_data)
            print(section)
            print(form.cleaned_data)
            messages.success(request, "Added")
            return redirect('section-list')
    else:
        form = SectionForm()
    return render(request, 'section/section_add.html',
                  {'form': form})


def section_edit(request, section_id):
    section = get_object_or_404(Section, pk=section_id)
    if request.method == "POST":
        form = SectionForm(request.POST, instance=section)
        if form.is_valid():
            section = form.save(commit=False)
            section.name = form.cleaned_data['name']
            section.departament = form.cleaned_data['departament']
            section.save()
            return redirect('section-list')
    else:
        form = SectionForm(instance=section)
    return render(request, 'section/section_edit.html',
                  {'form': form})


def section_delete(request, section_id):
    section = get_object_or_404(Section, pk=section_id)
    try:
        section.delete()
    except ProtectedError:
        messages.warning(request, 'Section has related objects and can not be deleted')
    return redirect('section-list')
