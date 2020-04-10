from .models import Departament, Student, Section, Contact

from django import forms


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    first_name = forms.CharField(
        max_length=64, label='Имя', widget=forms.TextInput(
            attrs={'id': 'f_name', 'required': True,
                   'placeholder': 'First name',
                   'class': 'form-control', 'type': 'text', }))

    last_name = forms.CharField(
        max_length=64, label='Фамилия', widget=forms.TextInput(
            attrs={'id': 'l_name', 'required': True,
                   'placeholder': 'Last name',
                   'class': 'form-control', 'type': 'text', }))

    second_name = forms.CharField(
        max_length=64, label='Отчество', widget=forms.TextInput(
            attrs={'id': 'p_name', 'required': True,
                   'placeholder': 'Second name',
                   'class': 'form-control', 'type': 'text', }))

    section = forms.ModelChoiceField(queryset=Section.objects.all(), empty_label=None,
                                     label='Отдел', widget=forms.Select(
            attrs={'id': 'department', 'class': 'form-control'}), )

    def clean_name(self):
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        second_name = self.cleaned_data['second_name']
        qs = Student.objects.filter(first_name=first_name, last_name=last_name, second_name=second_name)
        if qs.exists() and self.instance:
            qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError(
                f'student {self.first_name} {self.last_name} {self.second_name} already exists',
                code='invalid')
        return first_name


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = '__all__'

    name = forms.CharField(
        max_length=64, label='Название', widget=forms.TextInput(
            attrs={'id': 'name', 'required': True,
                   'placeholder': 'Department name',
                   'class': 'form-control', 'type': 'text', }))

    departament = forms.ModelChoiceField(queryset=Departament.objects.all(), empty_label=None,
                                         label='Департамент', widget=forms.Select(
            attrs={'id': 'name', 'class': 'form-control'}), )

    def clean_name(self):
        name = self.cleaned_data['name']
        qs = Section.objects.filter(name=name)
        if qs.exists() and self.instance:
            qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError('Section with name %(name)s already exists', params={'name': name},
                                        code='invalid')
        # raise forms.ValidationError(self.error_messages['password_mismatch'])
        return name

        # error_messages = {
        #     'password_mismatch': _("The two password fields didn't match."),
        # }


class DepartamentForm(forms.ModelForm):
    class Meta:
        model = Departament
        fields = '__all__'

    name = forms.CharField(
        max_length=128, label='Название', widget=forms.TextInput(
            attrs={'id': 'name', 'required': True,
                   'placeholder': 'Enterprise name',
                   'class': 'form-control', 'type': 'text', }))

    def clean_name(self):
        name = self.cleaned_data['name']
        qs = Departament.objects.filter(name=name)
        if qs.exists() and self.instance:
            qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError('Departament with name %(name)s already exists', params={'name': name})
        return name


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    student = forms.ModelChoiceField(queryset=Student.objects.all(), empty_label=None,
                                     label='Студент', widget=forms.Select(
            attrs={'id': 'name', 'class': 'form-control'}), )

    def clean_name(self):
        contact_type = self.cleaned_data['contact_type']
        value = self.cleaned_data['value']
        primary = self.cleaned_data['primary']
        qs = Section.objects.filter(type=contact_type, value=value, primary=primary)
        if qs.exists() and self.instance:
            qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError('Contact with value %(value)s already exists',
                                        params={'type': contact_type, 'value': value, 'primary': primary},
                                        code='invalid')
        # raise forms.ValidationError(self.error_messages['password_mismatch'])
        return value
