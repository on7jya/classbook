from django.db import models


class Departament(models.Model):
    """Департамент"""
    departament_name = models.CharField(max_length=100, verbose_name='Департамент')

    def __str__(self):
        return self.departament_name


class Division(models.Model):
    """Отдел - у департамента может быть несколько отделов"""
    division_name = models.CharField(max_length=100, verbose_name='Отдел')
    departament = models.ForeignKey(Departament, on_delete=models.CASCADE, verbose_name='Ссылка на id департамента')

    def __str__(self):
        return self.division_name


class Student(models.Model):
    """"Сотрудники - у сотрудника только одно место работы"""
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    second_name = models.CharField(max_length=50, verbose_name='Отчество')
    division = models.ForeignKey(Division, on_delete=models.CASCADE, verbose_name='Ссылка на id отдела')

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.second_name}"


class Contact(models.Model):
    """Контакты сотрудников - у сотрудника может быть несколько контактов"""
    phone = models.CharField(max_length=15, default='', verbose_name='Телефон')
    email = models.CharField(max_length=100, default='', verbose_name='Email')
    main_contact = models.BooleanField(max_length=1, default=False, verbose_name='Признак главного контакта')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Ссылка на id сотрудника')

    def __str__(self):
        if self.main_contact:
            return self.phone
        return self.email
