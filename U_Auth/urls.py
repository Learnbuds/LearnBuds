from django.urls import path
from U_Auth import views

urlpatterns = [
    path('sign-in/',views.sign_in,name='sign-in'),
    path('change-password/',views.changepassword,name='change-password'),
    path('sign-out/',views.signout,name='sign-out'),
]