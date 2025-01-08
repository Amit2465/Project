from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import EmployeeDetails 

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        retype_password = request.POST['retype_password']
        role = request.POST['role']

        # Password confirmation check
        if password != retype_password:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        # Check if the email already exists
        if EmployeeDetails.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('register')

        # Create new user
        user = EmployeeDetails.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,  # In a real application, hash the password before storing
            role=role
        )
        messages.success(request, "Registration successful! You can now log in.")
        return redirect('login')
    
    return render(request, 'register.html')


def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = EmployeeDetails.objects.get(email=email, password=password)
            # Store user in session
            request.session['user_id'] = user.id
            if user.role == "Admin":
                return redirect('task:admin_dashboard')
            else:
                return redirect('task:employee_dashboard')
        except EmployeeDetails.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid email or password'})

    return render(request, 'login.html')
