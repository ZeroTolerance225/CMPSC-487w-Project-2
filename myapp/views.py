from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import EmployeeForm
from .models import Employee
from django.shortcuts import get_object_or_404


def home(request):
    employees = Employee.objects.all()  # Fetch all employees

    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        employees = employees.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))

    # Sort functionality
    sort_by = request.GET.get('sort_by', '')
    if sort_by:
        employees = employees.order_by(sort_by)

    # Delete functionality
    delete_id = request.POST.get('delete_id')
    if request.method == 'POST' and delete_id:
        employee_to_delete = Employee.objects.filter(id=delete_id).first()
        if employee_to_delete:
            employee_to_delete.delete()

    # Add/Edit employee functionality
    if request.method == 'POST' and not delete_id:  # Ensure it's not a delete request
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page after saving
    else:
        form = EmployeeForm()

    return render(request, 'home.html', {'employees': employees, 'form': form})


def edit_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'edit_employee.html', {'form': form, 'employee': employee})
