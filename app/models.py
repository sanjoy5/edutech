from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Course(models.Model):
    instructor = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    topic = models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=200,null=True)
    description = models.TextField(null=True,blank=True) 
    # students = 
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-update','-created']
    
    def __str__(self):
        return self.title
    

class Chat(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    body = models.TextField()
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-update','-created']

    def __str__(self):
        return self.body
