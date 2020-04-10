"""classbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import views, views_student, views_section, views_departament, views_contact

urlpatterns = [
    path('', views.homepage_view, name="homepage"),

    path(r"api/v1/students/json/", views_student.students_list_json, name="student-list-json"),
    path(r'api/v1/students/<int:user_id>/json/', views_student.student_info_json,
         name="student-detail-json"),

    path(r'api/v1/students/list/', views_student.student_list, name='student-list'),
    path(r'api/v1/students/add/', views_student.student_add, name='student-add'),
    path(r'api/v1/students/<int:user_id>/edit/', views_student.student_edit, name='student-edit'),
    path(r'api/v1/students/<int:user_id>/delete/', views_student.student_delete, name='student-delete'),

    path(r'api/v1/section/list/', views_section.section_list, name='section-list'),
    path(r'api/v1/section/add/', views_section.section_add, name='section-add'),
    path(r'api/v1/section/<int:section_id>/edit/', views_section.section_edit, name='section-edit'),
    path(r'api/v1/section/<int:section_id>/delete/', views_section.section_delete, name='section-delete'),

    path(r'api/v1/departament/list/', views_departament.departament_list, name='departament-list'),
    path(r'api/v1/departament/add/', views_departament.departament_add, name='departament-add'),
    path(r'api/v1/departament/<int:departament_id>/edit/', views_departament.departament_edit, name='departament-edit'),
    path(r'api/v1/departament/<int:departament_id>/delete/', views_departament.departament_delete,
         name='departament-delete'),

    path(r'api/v1/contact/list/', views_contact.contact_list, name='contact-list'),
    path(r'api/v1/contact/add/', views_contact.contact_add, name='contact-add'),
    path(r'api/v1/contact/<int:contact_id>/edit/', views_contact.contact_edit, name='contact-edit'),
    path(r'api/v1/contact/<int:contact_id>/delete/', views_contact.contact_delete, name='contact-delete'),
]
