from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('location/', views.location, name='location'),
    path('programs/', views.programs, name='programs'),
    path('students/', views.students, name='students'),
    path('teachers/', views.teachers, name='teachers'),
    path('schools/', views.schools, name='schools'),
    path('insert_students/', views.insert_students, name='insert_students')

]
