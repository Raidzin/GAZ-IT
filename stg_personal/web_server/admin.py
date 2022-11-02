from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Department, Employee, Job, Sale

admin.site.unregister(Group)


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'type',
    search_fields = 'name',
    list_filter = 'type',


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'last_name', 'first_name', 'middle_name',
        'birth_date', 'birth_place'
    )
    search_fields = 'last_name', 'first_name', 'middle_name'
    list_filter = 'birth_place',


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'hire_date', 'dismiss_date', 'salary',
        'bonus', 'employee', 'chief', 'department'
    )
    search_fields = 'title', 'employee', 'chief', 'department'
    list_filter = (
        'title', 'employee', 'chief', 'department'
    )


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = 'id', 'date', 'amount', 'employee'
    search_fields = 'employee', 'amount'
    list_filter = 'date', 'employee'
