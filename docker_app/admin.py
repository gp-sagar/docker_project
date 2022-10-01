from django.contrib import admin
from .models import student

# Register your models here.
@admin.register(student)
class Student(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',]
