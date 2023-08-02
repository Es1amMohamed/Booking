from django.forms import SplitDateTimeField
from django.shortcuts import redirect, render
from .models import *
from django.core.paginator import Paginator
from .booking_func.availability import *
from .forms import *


# Create your views here.


def unit_list(request):
    units = Unit.objects.all()  
    paginator = Paginator(units,1)
    page = request.GET.get('page')
    page_ogj = paginator.get_page(page)
    context = {'units':page_ogj}   
    return render(request,'unit/unit_list.html',context)


def unit_detail(request,slug):
    unit = Unit.objects.get(slug=slug)
    
    if request.method == 'POST':
        form = UnitBookForm(request.POST)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.unit = unit
            my_form.user = request.user
            my_form.save()
            return redirect('/unit')
    else:
         form = UnitBookForm() 
         
    context = {"unit":unit,'form':form}
    return render(request,'unit/unit_detail.html',context)