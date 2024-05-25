from django.shortcuts import render
from Dating import views
from django.contrib.auth.decorators import login_required,user_passes_test

# Create your views here.

@user_passes_test(lambda u: u.is_staff,login_url='sign-in')
def index(request):
    context = {
        'page' : 'dating'
    }
    return render(request,'Dashboard/Dating/index.html',context)