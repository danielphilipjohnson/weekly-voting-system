
from django.db import models
import os
from ...models import Employee, Winner
import json

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to generate dummy users."""

    def handle(self,*args, **options):
      dir_path = os.path.dirname(os.path.realpath(__file__))
      json_file = dir_path+'/dummy_data.json'

      with open(json_file, 'r') as myfile:
        data=myfile.read()
    
      
      employees = json.loads(data)

      for employee in employees:
          employee_name = employee["name"]
          employee_nickname = employee["nickname"]

          employee_obj = Employee.objects.create(name=employee_name, nickname=employee_nickname)
          Winner.objects.create(employee=employee_obj, score=0)
          employee_obj.save()
      return "Employees seeded into the database!"

  