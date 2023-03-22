from django.urls import path
from . import views

urlpatterns = [
    path('',views.homePage,name='home'),
    path('course/<str:pk>/',views.coursePage,name='course'),

    path('create-course/',views.createCourse,name='create_course'),
    path('update-course/<str:pk>/',views.updateCourse,name='update_course'),
    path('delete-course/<str:pk>/',views.deleteCourse,name='delete_course'),
    path('delete-chat/<str:pk>/',views.deleteChat,name='delete_chat'),
]
