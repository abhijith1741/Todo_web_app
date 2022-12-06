
from django.contrib import admin
from django.urls import path, include

from todoApp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('update/<int:id>', views.update, name='update')

]