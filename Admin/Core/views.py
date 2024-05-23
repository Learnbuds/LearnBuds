from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

#----------------------------------- DASHBOARD -----------------------------------#

@login_required
def dashboard(request):
    return render(request,'Dashboard/Core/dashboard.html')