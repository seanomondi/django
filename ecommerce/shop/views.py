from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse('Home')


def about(request):
    return HttpResponse('About')


def contact(request):
    return HttpResponse('Contact')


def cart(request):
    return HttpResponse('Cart')


def products(request):
    return HttpResponse('Products')
