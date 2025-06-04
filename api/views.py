from employees.models import employee
from django.http import Http404
from django.shortcuts import get_object_or_404

#rest_framework
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins,generics,viewsets
from .serializers import StudentSerializer,employeeSerializer
from rest.models import SerializerModel




# Create your views here.
@api_view(['GET','POST'])
def studen(request):
    if request.method == 'GET':
        students = SerializerModel.objects.all()
        serialize =StudentSerializer(students,many=True)
    
        return Response(serialize.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serialize = StudentSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data,status=status.HTTP_201_CREATED)
        return Response(serialize.error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def student(request,pk):
    try:
        student = SerializerModel.objects.get(pk=pk)
    except SerializerModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serialize = StudentSerializer(student)
        return Response(serialize.data,status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serialize = StudentSerializer(student,data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data,status=status.HTTP_200_OK)
        else:
            return Response(serialize.data,status=status.HTTP_404_NOT_FOUND)
        
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
    

# class getemployee(APIView):
#     def get(self, request):
#         employ = employee.objects.all()
#         serializer = employeeSerializer(employ,many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serialize = employeeSerializer(data=request.data)
#         if serialize.is_valid():
#             serialize.save()
#             return Response(serialize.data,status=status.HTTP_201_CREATED)
#         return Response(serialize.error,status=status.HTTP_400_BAD_REQUEST)
    
# class singlemployee(APIView):
#     def get_object(self,pk):
#         try:
#             return employee.objects.get(pk=pk)
#         except employee.DoesNotExist:
#           raise Http404
    
#     def get(self, request,pk):
#         employee = self.get_object(pk)
#         serializer  = employeeSerializer(employee)
#         return Response(serializer.data,status=status.HTTP_200_OK)

#     def put(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = employeeSerializer(employee, data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)

# def delete(self, request, pk):
#     employee = self.get_object(pk)
#     employee.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)


"""
mixins
=======================================
class getemployee(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = employee.objects.all()
    serializer_class = employeeSerializer

    def get(self, request):
        return self.list(request)
    def post(self, request):
        return self.create(request)
    

class singlemployee(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = employee.objects.all()
    serializer_class = employeeSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    def delete(self, request, pk):
        return self.destroy(request, pk)
"""

# generics(single generic api views)
# class getemployee(generics.ListAPIView,generics.CreateAPIView):
#     queryset = employee.objects.all()
#     serializer_class = employeeSerializer

# class singlemployee(generics.RetrieveUpdateDestroyAPIView):
#     queryset = employee.objects.all()
#     serializer_class = employeeSerializer
#     lookup_field = 'pk'

#multiple generic apic views

# class getemployee(generics.ListCreateAPIView):
#     queryset = employee.objects.all()
#     serializer_class = employeeSerializer


class EmployeeViewset(viewsets.ViewSet):
    def list(self, request):
        queryset = employee.objects.all()
        serializer_class = employeeSerializer(queryset, many=True)
        return Response(serializer_class.data)
    
    def create(self, request):
        serializer = employeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    def retrieve(self, request, pk=None):
        employee_dtl = get_object_or_404(employee, pk=pk)
        serializer = employeeSerializer(employee_dtl)
        return Response(serializer.data, status=status.HTTP_200_OK)

        

