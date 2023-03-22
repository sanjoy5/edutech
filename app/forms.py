from django.forms import ModelForm
from .models import *

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        exclude = ['instructor','students']
        