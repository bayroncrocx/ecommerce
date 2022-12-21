from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('myFirstChart/', views.myFirstChart , name="myFirstChart"),
   #path('myFirstChart/<int:year>', views.myFirstChart , name="myFirstChart"),
   path('chart/', views.chart , name="chart"),
]