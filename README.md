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

new_dep_1 = Departament(name='Департамент по информационным технологиям')
new_dep_1.save()
new_dep_2 = Departament(name='Департамент по большим данным')
new_dep_2.save()
 
 

 
Section.objects.all()

new_division_1 = Section(departament=Departament(1), name='Отдел GK')
new_division_1.save()
new_division_2 = Section(departament=Departament(1), name='Бахус')
new_division_2.save()
new_division_3 = Section(departament=Departament(1), name='Комарх')
new_division_3.save()
new_division_4 = Section(departament=Departament(2), name='Отдел спроса')
new_division_4.save()
 
 
Student.objects.all()

new_student_1 = Student(last_name='Иванов', first_name='Иван', second_name='Иванович', section=Section(1))
new_student_1.save()
new_student_2 = Student(last_name='Петров', first_name='Петр', second_name='Петрович', section=Section(2))
new_student_2.save()
new_student_3 = Student(last_name='Сидоров', first_name='Сидор', second_name='Сидорович', section=Section(3))
new_student_3.save()
new_student_4 = Student(last_name='Джарабеков', first_name='Сигизмунд', second_name='Арасьевич', section=Section(4))
new_student_4.save()
 
 
Contact.objects.all()

new_contact_1 = Contact(student=Student(1), type='PHONE', value='111-111-111', primary = True)
new_contact_1.save()
new_contact_2 = Contact(student=Student(1), type='EMAIL', value='11@66666.ru', primary = False)
new_contact_2.save()
new_contact_3 = Contact(student=Student(2), type='PHONE', value='222-222-222', primary = True)
new_contact_3.save()
new_contact_4 = Contact(student=Student(3), type='EMAIL', value='333-333-333', primary = True)
new_contact_4.save() 
 ```
