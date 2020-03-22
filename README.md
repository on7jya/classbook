# classbook

python django-admin.py startproject classbook

cd ./classbook/
 
python manage.py startapp main

python manage.py runserver

python manage.py makemigrations

python manage.py sqlmigrate students 0001
 
python manage.py migrate

python manage.py shell 

from students.models import Fio
Fio.objects.all()
new_student = Fio(last_name='Иванов', first_name='Иван', second_name='Иванович')
new_student = Fio(last_name='Петров', first_name='Петр', second_name='Петрович')
new_student = Fio(last_name='Сидоров', first_name='Сидор', second_name='Сидорович')
new_student.save()

python manage.py createsuperuser