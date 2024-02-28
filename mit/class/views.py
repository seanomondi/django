from django.shortcuts import render
from django.http import HttpResponse

from . models import Student, Teacher, School

# Create your views here.


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def location(request):
    return render(request, 'location.html')


def programs(request):
    return render(request, 'programs.html')


def students(request):
    student = Student.objects.all()
    return render(request, 'students.html', {"students": student})


def teachers(request):
    teacher = Teacher.objects.all()
    return render(request, 'teachers.html', {"teachers": teacher})


def schools(request):
    school = School.objects.all()
    return render(request, 'schools.html', {"schools": school})


def insert_students(request):
    return render(request, 'insert_students.html')
