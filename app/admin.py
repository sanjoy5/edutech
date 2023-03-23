from django.contrib import admin
from .models import Course,Chat,Topic,User

# Register your models here.

admin.site.register(User)
admin.site.register(Topic)
admin.site.register(Course)
admin.site.register(Chat)
