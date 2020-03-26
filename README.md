# classbook

- $ python django-admin.py startproject classbook

- $ cd ./classbook/
 
- $ python manage.py startapp main

- $ python manage.py runserver

- $ python manage.py makemigrations

- $ python manage.py sqlmigrate students 0001
 
- $ python manage.py migrate

- $ python manage.py shell 

```sh
from students.models import *

 
Departament.objects.all()

new_dep_1 = Departament(departament_name='Департамент по информационным технологиям')
new_dep_1.save()
new_dep_2 = Departament(departament_name='Департамент по большим данным')
new_dep_2.save()
 
 

 
Division.objects.all()

new_division_1 = Division(departament=Departament(1), division_name='Отдел GK')
new_division_1.save()
new_division_2 = Division(departament=Departament(1), division_name='Бахус')
new_division_2.save()
new_division_3 = Division(departament=Departament(1), division_name='Комарх')
new_division_3.save()
new_division_4 = Division(departament=Departament(2), division_name='Отдел спроса')
new_division_4.save()
 
 
Student.objects.all()

new_student_1 = Student(last_name='Иванов', first_name='Иван', second_name='Иванович', division=Division(1))
new_student_1.save()
new_student_2 = Student(last_name='Петров', first_name='Петр', second_name='Петрович', division=Division(2))
new_student_2.save()
new_student_3 = Student(last_name='Сидоров', first_name='Сидор', second_name='Сидорович', division=Division(3))
new_student_3.save()
new_student_4 = Student(last_name='Джарабеков', first_name='Сигизмунд', second_name='Арасьевич', division=Division(4))
new_student_4.save()
 
 
Contact.objects.all()

new_contact_1 = Contact(student=Student(1), phone='111-111-111', email='11@11.ru', main_contact = True)
new_contact_1.save()
new_contact_2 = Contact(student=Student(1), phone='', email='11@66666.ru', main_contact = False)
new_contact_2.save()
new_contact_3 = Contact(student=Student(2), phone='222-222-222', email='222@222.ru', main_contact = True)
new_contact_3.save()
new_contact_4 = Contact(student=Student(3), phone='333-333-333', email='333@333.ru', main_contact = True)
new_contact_4.save()
new_contact_5 = Contact(student=Student(4), phone='444-444-444', email='444@444.ru', main_contact = True)
new_contact_5.save()
 ```
