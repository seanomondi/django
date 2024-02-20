from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('about/', views.about),
    path('contact/', views.contact),
    path('location/', views.location),
    path('programs/', views.programs)

]
