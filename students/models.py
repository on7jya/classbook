from django.db import models


class Departament(models.Model):
    """Департамент"""
    name = models.CharField(max_length=100, verbose_name='Департамент')

    class Meta:
        verbose_name = "Департамент"
        verbose_name_plural = "Департаменты"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Section(models.Model):
    """Отдел - у департамента может быть несколько отделов"""
    name = models.CharField(max_length=100, verbose_name='Отдел')
    departament = models.ForeignKey(Departament, on_delete=models.CASCADE, verbose_name='Департамент')

    class Meta:
        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Student(models.Model):
    """"Сотрудники - у сотрудника только одно место работы"""
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    second_name = models.CharField(max_length=30, verbose_name='Отчество')
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name='Отдел')

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"
        ordering = ["last_name", "first_name", "second_name"]

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.second_name}"

    def to_json(self):
        return {
            "id": self.pk,
            "last_name": self.last_name,
            "first_name": self.first_name,
            "second_name": self.second_name,

            "section_id": self.section.pk,
            "section_name": self.section.name,
        }


class Contact(models.Model):
    """Контакты сотрудников - у сотрудника может быть несколько контактов"""
    PHONE = "phone"
    EMAIL = "email"
    type = models.CharField("Тип", max_length=5, choices=((PHONE, "Телефон"), (EMAIL, "E-mail")))
    value = models.CharField("Значение", max_length=30)
    primary = models.BooleanField("Основной", default=False, blank=True)
    student = models.ForeignKey(Student, verbose_name="Студент", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        unique_together = ('student', 'primary', 'type')

    def __str__(self):
        return self.value
