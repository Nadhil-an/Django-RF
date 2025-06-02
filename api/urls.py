from django.urls import path
from . import views


urlpatterns = [
    path('studen/', views.studen),
    path('student/<int:pk>/',views.student),
]