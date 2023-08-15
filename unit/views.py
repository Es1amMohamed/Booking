from django.forms import SplitDateTimeField
from django.shortcuts import redirect, render
from .models import *
from django.core.paginator import Paginator
from .booking_func.availability import *
from .forms import *
from django.utils import timezone

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
            if check_availability(unit,my_form.date_from,my_form.date_to):
                now = timezone.now().date()
                if now <= my_form.date_from and now <= my_form.date_to :
                    my_form.save()
                    date_to = my_form.date_to 
                    date_from= my_form.date_from 
                    unit = my_form.unit
                    context = {
                        'date_to':date_to,
                        'date_from':date_from,
                        'unit':unit,
                    }
                    return render(request,'unit/available.html',context)
                else:
                    not2 = 'Not valid date'
                    return render(request,'unit/not_available.html',{'not4':not2} )
            else:
                not3 = 'gg'
                return render(request,'unit/not_available.html',{'not1':not3} )

            
    else:
         form = UnitBookForm() 
         
    context = {"unit":unit,'form':form}
    return render(request,'unit/unit_detail.html',context)

