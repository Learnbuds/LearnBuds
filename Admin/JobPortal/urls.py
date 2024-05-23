from django.urls import path
from JobPortal import views

urlpatterns = [
    path('',views.index,name='jobportal-index')
]