from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        exclude = ['instructor','students']
        