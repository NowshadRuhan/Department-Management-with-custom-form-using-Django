from django.shortcuts import render
from django.http import HttpResponse

#import models thats i Create
from Second_app.models import Department, Teachers, Students

#import forms
from Second_app import second_forms


# Create your views here.
def home(request):

    department_list = Department.objects.order_by('id')

    teacher_list = Teachers.objects.order_by('id')

    students_list = Students.objects.order_by('id')

    diction = {
        'department_list': department_list,
        'teacher_list': teacher_list,
        'students_list': students_list,
        'name': 'Md. Nowshad Ruhani Chowdhury',
    }
    return render(request, 'Second_app/home.html', context=diction)


def form(request):

    department_form = second_forms.DepartmentForm()
    TeachersForm = second_forms.TeachersForm()
    if request.method == "POST":
        department_form = second_forms.DepartmentForm(request.POST)

        if department_form.is_valid():
            department_form.save(commit=True)

            return home(request)

    data = {
        'department_title': 'Department Add Form By Django',
        'department_form':department_form,

        'teacher_title': 'Teacher Add Form By Django',
        'TeachersForm': TeachersForm,

        'students_title': 'Student Add Form By Django',
    }



    return render(request, 'Second_app/second_form.html', context=data)
