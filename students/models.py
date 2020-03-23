from django.db import models


# Create your models here.
class Fio(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)


class Contact(models.Model):
    student = models.ForeignKey(Fio, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    main_contact = models.BooleanField(max_length=1)

    def __str__(self):
        if self.main_contact:
            return self.telephone
        elif not self.main_contact:
            return self.email


class PlaceWork(models.Model):
    student = models.ForeignKey(Fio, on_delete=models.CASCADE)
    departament = models.TextField(default='Корпоративный центр X5')
    division = models.TextField(default='Отдел бизнес-приложений GK')

    def __str__(self):
        return self.departament
