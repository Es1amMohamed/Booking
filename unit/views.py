from django.forms import SplitDateTimeField
from django.shortcuts import redirect, render
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
    if request.method == 'POST':
        print("in post")
        check_in = request.POST.get('check_in')
        print(list(check_in))
        check_out = request.POST.get('check_out')
        adults = request.POST.get("adults")
        children = request.POST.get("children")
        data = UnitBook(user= request.user,unit=unit,date_from=check_in,date_to=check_out ,adults=adults,children=children)
        data.save()
        return redirect('/unit')
        
    else:
         print("in else")
         unit = Unit.objects.get(slug=slug) 
    
    
    
    return render(request,'unit/unit_detail.html',context)