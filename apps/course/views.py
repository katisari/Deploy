from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.core.urlresolvers import reverse
from django.contrib import messages
# from django.contrib import messages

def index(request):
    all_courses = Course.objects.all()
    content = {
        'all_courses':all_courses
    }
    return render(request, 'course/index.html', content)

def destroy(request, id):
    content = {
        'course_info': Course.objects.get(id=id)
    }
    return render(request, 'course/destroy.html', content)

def create(request):
    if request.method == "POST":
        direct_main = False
        if len(request.POST['name']) < 5:
            direct_main = True
            messages.warning(request, 'Fill out your name properly')
        if len(request.POST['desc']) < 15:
            direct_main = True
            messages.warning(request, 'Description should be more than 15 characters') 
        if direct_main:
            return redirect(reverse('main_page'))        
        Course.objects.create(name=request.POST['name'], desc=request.POST['desc'])
        messages.success(request, "User has been added")

    return redirect(reverse('main_page'))

def process_destroy(request, id):
    print("got in")
    b = Course.objects.get(id=id)
    b.delete()
    return redirect(reverse('main_page'))