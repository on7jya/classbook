import json
from django.http import HttpResponse
from django.shortcuts import render

from students.models import Student, Contact, Division, Departament


def get_homepage(request):
    """Домашняя страница"""
    return render(request=request, template_name="main/home.html")


def get_students_list(request):
    """Получить список студентов"""
    # 1. вариант через шаблон
    # return render(request=request,
    #               template_name="main/students_list.json",
    #               context={"students": Student.objects.all})

    # 2. через serializers
    # students = Student.objects.all()
    # data = serializers.serialize('json', students)
    # return HttpResponse(data, content_type='application/json')

    # 3. через json.dumps
    response_data = Student.objects.all().values()
    return HttpResponse(json.dumps(list(response_data)), content_type='application/json')


def get_student_info(request, user_id):
    """Получить всю информацию о студенте"""
    student_queryset = Student.objects.filter(id=user_id)
    contact_queryset = Contact.objects.filter(student_id=user_id)
    div = dep = ''
    for student in student_queryset:
        div = student.division_id
    div_queryset = Division.objects.filter(id=div)
    for division in div_queryset:
        dep = division.departament_id
    dep_queryset = Departament.objects.filter(id=dep)
    all_objects = [*student_queryset.values(), *contact_queryset.values(),
                   *div_queryset.values(), *dep_queryset.values()]
    return HttpResponse(json.dumps(list(all_objects)), content_type='application/json')
