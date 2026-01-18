from django.urls import path
from . import views

urlpatterns =[
    path('student/',views.studentsViews),
    path('student/<int:pk>/',views.studentDetailview),

    path('employee/',views.Employees.as_view())

]