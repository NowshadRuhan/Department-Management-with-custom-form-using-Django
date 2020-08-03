from django.db import models

from django import forms

# Create your models here.
class Department(models.Model):
    #id auto included
    department_name = models.CharField(max_length=100)
    department_code = models.CharField(max_length = 50)
    department_num_course = models.IntegerField()

    def __str__(self):
        return self.department_name +", "+ self.department_code +", "+ str(self.department_num_course)


class Teachers(models.Model):
    #id auto included
    department_teacher = models.ForeignKey(Department, on_delete=models.CASCADE)
    teacher_full_name = models.CharField(max_length=100)
    teacher_username = models.CharField(max_length=50)
    teacher_city = models.CharField(max_length=50)
    teacher_country = models.CharField(max_length=50)
    teacher_phone = models.IntegerField()
    teacher_address = models.CharField(max_length=100)

    def __str__(self):
        return self.teacher_full_name +", "+ self.teacher_username +", "+ self.teacher_city+", "+ self.teacher_country +", "+ str(self.teacher_phone)+", "+ self.teacher_address




class Students(models.Model):
    #id auto included
    department_student = models.ForeignKey(Department, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=50)
    city_name = models.CharField(max_length=50)
    country_name =models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.IntegerField()

    def __str__(self):
        return self.full_name +", "+ self.user_name +", "+ self.city_name+", "+ self.country_name +", "+ self.address+", "+ str(self.phone)
