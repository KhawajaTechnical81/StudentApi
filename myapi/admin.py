from django.contrib import admin

from myapi.models import Student

@admin.register(Student)
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']