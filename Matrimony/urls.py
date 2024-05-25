from django.urls import path
from Matrimony import views

urlpatterns = [
    path('',views.index,name='matrimony-index')
]