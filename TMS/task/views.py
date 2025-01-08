from django.shortcuts import render

# Create your views here.
def employee_dashboard(request):
    return render(request, 'employee_dashboard.html')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')