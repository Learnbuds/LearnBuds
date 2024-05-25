from django.urls import path
from Dating import views

urlpatterns = [
    path('',views.index,name='dating-index'),
]