from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import EmployeeSerializer
from voting.models import Employee

class EmployeeList(APIView):
    def get(self, request, *args, **kwargs):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    