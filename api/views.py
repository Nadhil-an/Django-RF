from rest_framework.response import Response
from .serializers import StudentSerializer
from rest.models import SerializerModel
from rest_framework import status
from rest_framework.decorators import api_view
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