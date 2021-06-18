from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import EmployeeSerializer, WinnerSerializer
from voting.models import Employee, Winner

class EmployeeList(APIView):
    def get(self, request, *args, **kwargs):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class WinnersList(APIView):
    def get(self, request, *args, **kwargs):
        '''
        List all winners
        '''
        winners = Winner.objects.order_by('-score')
        serializer = WinnerSerializer(winners, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)