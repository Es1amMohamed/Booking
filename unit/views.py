from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator

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
    context = {"unit":unit}
    
    return render(request,'unit/unit_detail.html',context)