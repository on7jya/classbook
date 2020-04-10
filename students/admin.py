from django.contrib import admin

from .models import Student, Contact, Section, Departament


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 0


class StudentAdmin(admin.ModelAdmin):
    list_display = ["last_name", "first_name", "second_name", "section"]
    search_fields = ["last_name", "first_name", "second_name"]
    list_filter = ["section"]
    inlines = [
        ContactInline
    ]


admin.site.register(Contact)
admin.site.register(Section)
admin.site.register(Departament)
admin.site.register(Student, StudentAdmin)
