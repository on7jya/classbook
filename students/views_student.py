from django.contrib import messages
from django.db.models import ProtectedError
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import StudentForm
from .models import Student


def students_list_json(request):
    """Получить список студентов"""
    # 1. вариант через шаблон
    # return render(request=request,
    #               template_name="main/students_list_json.json",
    #               context={"students": Student.objects.all})

    # 2. через serializers
    # students = Student.objects.all()
    # data = serializers.serialize('json', students)
    # return HttpResponse(data, content_type='application/json')

    # 3. через json.dumps и HttpResponse
    # response_data = Student.objects.all().values()
    # return HttpResponse(json.dumps(list(response_data)), content_type='application/json')

    # 4. без json.dumps и через JsonResponse
    students = list(Student.objects.all().values("pk", "last_name", "first_name", "second_name"))
    return JsonResponse({"students": students})


def student_info_json(request, user_id):
    """Получить всю информацию о студенте"""
    # student_queryset = Student.objects.filter(id=user_id)
    # contact_queryset = Contact.objects.filter(student_id=user_id)
    # div = dep = ''
    # for student in student_queryset:
    #     div = student.division_id
    # div_queryset = Section.objects.filter(id=div)
    # for division in div_queryset:
    #     dep = division.departament_id
    # dep_queryset = Departament.objects.filter(id=dep)
    # all_objects = [*student_queryset.values(), *contact_queryset.values(),
    #                *div_queryset.values(), *dep_queryset.values()]
    # return HttpResponse(json.dumps(list(all_objects)), content_type='application/json')

    # # student = get_object_or_404(Student, pk=id)  # два запроса к БД (второй ниже в .to_json())
    #
    student = get_object_or_404(Student.objects.select_related("section"), pk=user_id)  # JOIN, один запрос к БД
    #
    # # try:
    # #     student = Student.objects.select_related("department").get(pk=id)
    # # except Student.DoesNotExist:
    # #     raise Http404

    return JsonResponse(student.to_json())


def student_list(request):
    students = Student.objects.all().order_by('id')
    context = {'students': students, }
    return render(request, 'student/student_list.html', context)


def student_add(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.first_name = form.cleaned_data['first_name']
            student.last_name = form.cleaned_data['last_name']
            student.second_name = form.cleaned_data['second_name']
            student.section = form.cleaned_data['section']
            student.save()
            return redirect('student-list')
    else:
        form = StudentForm()
    return render(request, 'student/student_add.html', {'form': form})


def student_edit(request, user_id):
    student = get_object_or_404(Student, pk=user_id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            student = form.save(commit=False)
            student.first_name = form.cleaned_data['first_name']
            student.last_name = form.cleaned_data['last_name']
            student.second_name = form.cleaned_data['second_name']
            student.section = form.cleaned_data['section']
            student.save()
            return redirect('student-list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student/student_edit.html', {'form': form})


def student_delete(request, user_id):
    student = get_object_or_404(Student, pk=user_id)
    try:
        student.delete()
    except ProtectedError:
        messages.warning(request, 'student has related objects and can not be deleted')
    return redirect('student-list')
