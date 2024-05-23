from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def rocket(request):
    return render(request,'Error/Rocket.html')

def error_400(request,exception):
    return render(request,'Error/400.html')

def error_403(request,exception):
    return render(request,'Error/403.html')

def error_404(request,exception):
    return render(request,'Error/404.html')

def error_500(request):
    return render(request,'Error/500.html')