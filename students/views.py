from django.shortcuts import render

from students.models import *


def homepage(request):
    return render(request=request,
                  template_name="main/home.html")


def get_students_list(request):
    # return HttpResponse('здесь будет список студентов')
    return render(request=request,
                  template_name="main/students_list.json",
                  context={"students": Fio.objects.all})


def get_student_info(request, id):
    # return HttpResponse('здесь будет подробная информация о студенте')
    return render(request=request,
                  template_name="main/student_info.json",
                  context={"students": Fio(id=id),
                           'contacts': Contact(Fio(id=id)),
                           'placework': PlaceWork(Fio(id=id))})
