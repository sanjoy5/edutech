from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import * 
from django.db.models import Q
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        email = request.POST['email'].lower()
        password = request.POST['password']
        
        user = authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Login successfully')
            return redirect('home')
        else:
            messages.error(request,'email or password invalid!!!')

    return render(request,'login.html')


def logoutPage(request):
    logout(request)
    messages.success(request,'Logout Successfully')
    return redirect('login')

def homePage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    courses = Course.objects.filter(
        Q(topic__name__icontains=q) |
        Q(title__icontains=q) |
        Q(description__icontains=q) 
    )
    topics = Topic.objects.all()[:5]
    chats = Chat.objects.filter(Q(course__topic__name__icontains=q))
    total_course = courses.count()
    

    context = {'courses':courses,'topics':topics,'total_course':total_course,'chats':chats}
    return render(request,'app/home.html',context)


def coursePage(request,pk):
    course = Course.objects.get(id=pk)
    course_chats = course.chat_set.all()
    students = course.students.all()

    if request.method == "POST":
        Chat.objects.create(
            user = request.user,
            course = course,
            body = request.POST['body']
        )
        course.students.add(request.user)
        return redirect('course', pk=course.id)

    context = {'course':course,'course_chats':course_chats,'students':students}
    return render(request,'app/course.html',context)

@login_required(login_url='login')
def createCourse(request):
    page = 'create_course'
    form = CourseForm()
    if request.method == "POST":
        form = CourseForm(request.POST,request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.instructor = request.user
            course.save()
            return redirect('home')
        else:
            messages.error(request,'Something is Wrong!')
   

    context = {'form':form,'page':page}
    return render(request,'app/course_form.html',context)


@login_required(login_url='login')
def updateCourse(request,pk):
    course = Course.objects.get(id=pk)
    form = CourseForm(instance=course)
    if request.user != course.instructor:
        return HttpResponse('You are not allowed here!!')
    
    if request.method == "POST":
        form = CourseForm(request.POST,request.FILES,instance=course)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            messages.error(request,'Something is Wrong!')
   

    context = {'form':form}
    return render(request,'app/course_form.html',context)


@login_required(login_url='login')
def deleteCourse(request,pk):
    course = Course.objects.get(id=pk)
    if request.user != course.instructor:
        return HttpResponse('You are not allowed here!!')
    if request.method == "POST":
        course.delete()
        messages.success(request,'Course deleted successfully')
        return redirect('home')
    context = {'obj':course}
    return render(request,'delete.html',context)


@login_required(login_url='login')
def deleteChat(request,pk):
    chat = Chat.objects.get(id=pk)
    if request.user != chat.user:
        return HttpResponse('You are not allowed here!!')
    if request.method == "POST":
        chat.delete()
        messages.success(request,'Chat deleted successfully')
        return redirect('home')
    context = {'obj':chat}
    return render(request,'delete.html',context)


def topicsPage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = Topic.objects.filter(name__icontains=q)

    context = {'topics':topics}
    return render(request,'app/topics.html',context)

def activityPage(request):
    chats = Chat.objects.all()
    context = {'chats':chats}
    return render(request,'app/activities.html',context)