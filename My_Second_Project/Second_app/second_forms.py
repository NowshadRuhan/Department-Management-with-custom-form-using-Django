from django import forms
from django.forms import  Textarea, TextInput, NumberInput, ChoiceField
#import models
from Second_app import models


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = models.Department
        fields = ('department_name', 'department_code', 'department_num_course')
        widgets = {
            'department_name': TextInput(attrs={'class': 'input'}),
            'department_code': TextInput(attrs={'class': 'input'}),
            'department_num_course': NumberInput(attrs={'class': 'input'}),
        }
        labels = {
            "department_name": "Department Name ",
            "department_code": "Department Code ",
            "department_num_course": "Department Course ",
        }

class TeachersForm(forms.ModelForm):
    class Meta:
        model = models.Teachers
        fields = "__all__"

        choices = models.Department.objects.order_by('id')

        widgets = {
            
            'teacher_full_name': TextInput(attrs={'class': 'input'}),
            'teacher_username': TextInput(attrs={'class': 'input'}),
            'teacher_city': TextInput(attrs={'class': 'input'}),
            'teacher_country': TextInput(attrs={'class': 'input'}),
            'teacher_phone': NumberInput(attrs={'class': 'input'}),
            'teacher_address': TextInput(attrs={'class': 'input'})
        }
        labels = {
            "department_teacher": "Teacher Department ",
            "teacher_full_name": "Teacher Name ",
            "teacher_username": "Teacher Username ",
            "teacher_city": "Teacher City ",
            "teacher_country": "Teacher Country ",
            "teacher_phone": "Teacher Phone ",
            "teacher_address": "Teacher Address ",
        }
