from django.urls import path
from . import views


urlpatterns = [
    path('studen/', views.studen),
    path('student/<int:pk>/',views.student),

    path('employee/',views.getemployee.as_view()),
    path('employee/<int:pk>/',views.singlemployee.as_view())

]