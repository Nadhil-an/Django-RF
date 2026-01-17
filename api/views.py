from django.shortcuts import render
from django.http import JsonResponse
from student.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET','POST'])
def studentsViews(request):
    if request.method == 'GET':

        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':

        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        