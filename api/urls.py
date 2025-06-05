from django.urls import path,include
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees',views.EmployeeViewset)


urlpatterns = [
    path('studen/', views.studen),
    path('student/<int:pk>/',views.student),

    # path('employee/',views.getemployee.as_view()),
    # path('employee/<int:pk>/',views.singlemployee.as_view())

    path('',include(router.urls)),

    path('blogs/',views.blogviewset.as_view()),
    path('comments/',views.commentviewset.as_view()),

    path('blogs/<int:pk>/',views.BlogDetailsView.as_view()),
    path('comments/<int:pk>/',views.CommentDetailsView.as_view())



]