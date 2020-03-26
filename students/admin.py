from django.contrib import admin

from .models import Student, Contact, Division, Departament

admin.site.register(Student)
admin.site.register(Contact)
admin.site.register(Division)
admin.site.register(Departament)
