from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import EmployeeDetails

@admin.register(EmployeeDetails)
class EmployeeDetailsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'role')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('role',)
