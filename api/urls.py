from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('employees',views.EmployeeViewset,basename='employee')

urlpatterns =[
    path('student/',views.studentsViews),
    path('student/<int:pk>/',views.studentDetailview),

    # path('employee/',views.Employees.as_view()),
    # path('employee/<int:pk>/',views.EmployeesDetails.as_view()),

    path('',include(router.urls))


    

]