from rest_framework import serializers
from .models import Employee, Winner

class EmployeeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Employee 
    fields = '__all__'
    
class WinnerSerializer(serializers.ModelSerializer):
  employee = EmployeeSerializer(many=False)
  class Meta:
    model = Winner
    ordering = ['score']
    fields =  '__all__'
