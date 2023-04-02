from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutPage,name='logout'),
    path('register/',views.registerPage,name='register'),

    path('',views.homePage,name='home'),
    path('course/<str:pk>/',views.coursePage,name='course'),

    path('create-course/',views.createCourse,name='create_course'),
    path('update-course/<str:pk>/',views.updateCourse,name='update_course'),
    path('delete-course/<str:pk>/',views.deleteCourse,name='delete_course'),
    path('delete-chat/<str:pk>/',views.deleteChat,name='delete_chat'),

    path('topics/',views.topicsPage,name='topics'),
    path('activities/',views.activityPage,name='activities'),

    path('profile/<int:pk>/',views.userProfile,name='profile'),
    path('update-profile/',views.updateUser,name='update_profile'),


    path('password_reset/',auth_views.PasswordResetView.as_view(template_name="password_reset_form.html"),name='password_reset'),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"),name='password_reset_confirm'),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),name='password_reset_complete'),
    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),name='password_reset_complete'),
]
