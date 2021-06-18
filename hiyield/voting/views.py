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

    ## only implemented to allow users to be added
    ## can be disabled later
    def post(self, request, *args, **kwargs):
            data = {
                'name': request.data.get('name'), 
                'nickname': request.data.get('nickname'), 
            }

            employeeSerializer = EmployeeSerializer(data=data)
            
            if employeeSerializer.is_valid():
                user = employeeSerializer.save()
                winner = Winner(employee=user, score=0)
                winner.save()
             
                return Response(employeeSerializer.data, status=status.HTTP_201_CREATED)

            return Response(employeeSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WinnersList(APIView):
    def get(self, request, *args, **kwargs):
        '''
        List all winners
        '''
        winners = Winner.objects.order_by('-score')
        serializer = WinnerSerializer(winners, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def get_object(self, winner_id):
        try:
            return Winner.objects.get(pk=winner_id)
        except Winner.DoesNotExist:
            raise Http404

    def put(self, request, winner_id):
        # In practice would check 
        # permission_classes = [
        #     permissions.IsAuthenticated,
        # ]

        # then filter the object by request.user.id to possibly prevent people voting themselves
        winner_instance = self.get_object(winner_id)
        data = {
            "score": winner_instance.score + 1
        }

        serializer = WinnerSerializer(instance=winner_instance, data=data, partial = True)
       
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)