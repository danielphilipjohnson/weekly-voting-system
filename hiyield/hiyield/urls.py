from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from voting import views


urlpatterns = [
    path('api/employees/', views.EmployeeList.as_view()),
    path('api/winners/', views.WinnersList.as_view()),
    path('api/winner/<int:winner_id>', views.WinnerIncreaseScore.as_view()),
]
