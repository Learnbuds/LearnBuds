from django.urls import path
from ErrHandler import views

urlpatterns = [
    path('rocket/',views.rocket,name='rocket')
]