# classbook

- $ python django-admin.py startproject classbook

- $ cd ./classbook/
 
- $ python manage.py startapp main

- $ python manage.py runserver

- $ python manage.py makemigrations

- $ python manage.py sqlmigrate students 0001
 
- $ python manage.py migrate

- $ python manage.py shell 

`from students.models import *`

```sh
Fio.objects.all()

new_student = Fio(last_name='Иванов', first_name='Иван', second_name='Иванович')

new_student = Fio(last_name='Петров', first_name='Петр', second_name='Петрович')

new_student = Fio(last_name='Сидоров', first_name='Сидор', second_name='Сидорович')

new_student.save()
```
```sh
Contact.objects.all()

new_contact = Contact(student=Fio(1), telephone='111-111-111', email='111@111.ru', main_contact='1')

new_contact = Contact(student=Fio(2), telephone='222-222-222', email='222@222.ru', main_contact='0')

new_contact = Contact(student=Fio(3), telephone='333-333-333', email='333@333.ru', main_contact='1')

new_contact.save()
```
```sh
PlaceWork.objects.all()

new_placework = PlaceWork(student=Fio(1), departament='КЦ Х5', division='отдел бизнес приложений GK')

new_placework = PlaceWork(student=Fio(2), departament='КЦ Х5', division='отдел бизнес приложений GK')

new_placework = PlaceWork(student=Fio(3), departament='КЦ Х5', division='отдел бизнес приложений GK')

new_placework.save()
```