from django.contrib import admin
from .models import Course,Chat,Topic

# Register your models here.

admin.site.register(Topic)
admin.site.register(Course)
admin.site.register(Chat)
