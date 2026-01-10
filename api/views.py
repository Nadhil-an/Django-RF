from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def studentsViews(request):
    student = [
        {
            'id':'1',
            'name':'nadhil',
            'course':'cs'
        }
    ]
    return JsonResponse(student,safe=False)