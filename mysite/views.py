from django.http import HttpResponse
from django.shortcuts import render
from employees.models import Employee


def home(request):
    employeeList = Employee.objects.all()
    context = {
        'employees': employeeList,
    }
    return render(request, 'home.html', context)
