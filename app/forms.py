from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name','username','email','password1','password2']

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        exclude = ['instructor','students']
        

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar','name','username','email','bio']