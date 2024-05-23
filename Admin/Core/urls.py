from django.urls import path
from Core import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
]