from django.shortcuts import render
from .models import * 
from django.db.models import Q

# Create your views here.

def homePage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    courses = Course.objects.filter(
        Q(topic__name__icontains=q) |
        Q(title__icontains=q) |
        Q(description__icontains=q) 
    )
    topics = Topic.objects.all()
    chats = Chat.objects.filter(Q(course__topic__name__icontains=q))
    total_course = courses.count()
    

    context = {'courses':courses,'topics':topics,'total_course':total_course,'chats':chats}
    return render(request,'app/home.html',context)