from django.db import models

# Create your models here.

class Dept(models.Model):
    dept_no = models.IntegerField(primary_key=True)
    dept_name = models.CharField(max_length=100)
    loc = models.CharField(max_length=100)

    def __str__(self):
        return str(self.dept_no)

class Emp(models.Model):
    empno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=100)
    sal = models.IntegerField()
    job = models.CharField(max_length=100)
    deptno = models.ForeignKey(Dept, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.empno)
