from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required,user_passes_test

# Create your views here.

#----------------------------------- DASHBOARD -----------------------------------#

@user_passes_test(lambda u: u.is_staff,login_url='sign-in')
def dashboard(request):
    context = {
        'page' : 'dashboard'
    }
    return render(request,'Dashboard/Core/dashboard.html',context)