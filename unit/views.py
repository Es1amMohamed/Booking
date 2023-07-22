from django.shortcuts import render
from .models import *

# Create your views here.


def unit_list(request):
    units = Unit.objects.all()
    context = {'units':units}
    
    return render(request,'unit/unit_list.html',context)

def unit_detail(request,slug):
    unit = Unit.objects.get(slug=slug)
    context = {"unit":unit}
    
    return render(request,'unit/unit_detail.html',context)