from django.urls import path
from . import views

app_name = 'task'

urlpatterns = [
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('employee_dashboard/', views.employee_dashboard, name='employee_dashboard'),
]