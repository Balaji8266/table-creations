from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import *

def dept(request):
    QLDO = Dept.objects.all()
    d = {'dept' : QLDO}
    return render(request, 'dept.html', d)


def emp(request):
    QLEO = Emp.objects.all()
    d = {'emp' : QLEO}
    return render(request, 'emp.html', d)




def insert_emp(request):
    dno = int(input('Enter Dno : '))
    Empno = int(input('Enter Emp NO : '))
    Ename = input('Enter Emp Name: ')
    sal = int(input('Enter Salary : '))
    job = input('Enter Emp Job : ')

    DO = Dept.objects.get(dept_no = dno)
    NEO = Emp.objects.get_or_create(empno = Empno, ename = Ename, sal = sal, job = job, deptno = DO)[0]
    NEO.save()
    return render(request, 'emp.html')

def insert_dept(request):
    dno = int(input('Enter Dno : '))
    dname = input('Enter Department Name : ')
    loc = input('Enter Location : ')

    DNO = Dept.objects.get_or_create(dept_no = dno, dept_name = dname, loc = loc)[0]
    DNO.save()

    return render(request, 'dept.html')


