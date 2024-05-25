from django.shortcuts import render
from Matrimony import views
from django.contrib.auth.decorators import login_required,user_passes_test

# Create your views here.

@user_passes_test(lambda u: u.is_staff,login_url='sign-in')
def index(request):
    context = {
        'page' : 'matrimony'
    }
    return render(request,'Dashboard/Matrimony/index.html',context)