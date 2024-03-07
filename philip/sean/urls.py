from django.urls import path
from . import views


urlpatterns = [
    path('', views.clients, name='clients'),
    path('insert', views.insertData, name="insertData"),
    path('update/<id>', views.updateData, name="updateData"),
    path('delete/<id>', views.deleteData, name="deleteData")
]