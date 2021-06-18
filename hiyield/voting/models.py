from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100, blank=True)
    nickname = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

class Winner(models.Model):
    employee = models.ForeignKey(
        Employee, related_name='employee_winner', on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    
    def __str__(self):
        return self.employee
