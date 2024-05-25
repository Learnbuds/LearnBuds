from django.shortcuts import render
from Dating import views
from django.contrib.auth.decorators import login_required,user_passes_test

# Create your views here.

@user_passes_test(lambda u: u.is_superuser,login_url='sign-in')
def index(request):
    context = {
        'page' : 'jobportal'
    }
    return render(request,'Dashboard/JobPortal/index.html',context)