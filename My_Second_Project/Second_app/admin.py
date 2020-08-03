from django.contrib import admin

#import models
from Second_app.models import Department, Teachers, Students


# Register your models here.
admin.site.register(Department)
admin.site.register(Teachers)
admin.site.register(Students)
