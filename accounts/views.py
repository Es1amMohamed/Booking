
from django.shortcuts import redirect, render
from django.template import RequestContext
from .forms import SignupForm 
from django.contrib.auth import  login
from .models import *
from unit.models import *

# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        form = SignupForm(data=request.POST)  
        if form.is_valid():
            use = form.cleaned_data['username']
            em = form.cleaned_data['email']
            user = User.objects.create(username=use, email=em )
           # user.set_password(form.cleaned_data['password2'])
            user.save()
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/accounts/profile')

        
    else:
        form = SignupForm()
            


    return render(request, 'accounts/sginup.html',{'form':form})


def profile(request):
    
    profile = Profile.objects.get(user=request.user)
    return render(request, 'accounts/profile.html',{'profile':profile})


def edit_profile(request):
    pass



def my_reservation(request):
    unit_list = UnitBook.objects.filter(user= request.user)
    return render(request,'accounts/reservation.html',{'unit_list':unit_list})