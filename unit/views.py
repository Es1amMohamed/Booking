
from django.shortcuts import redirect, render
from .models import *
from django.core.paginator import Paginator
from .booking_func.availability import *
from .forms import *
from django.utils import timezone
from django.db.models import Max
from django.contrib.auth.decorators import login_required

# Create your views here.


def unit_list(request):
    units = Unit.objects.all()
    paginator = Paginator(units,1)
    page_num = request.GET.get('page')
    page_ogj = paginator.get_page(page_num)
    context = {'units':page_ogj}   
    return render(request,'unit/unit_list.html',context)


@login_required
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
                if now <= my_form.date_from and now <= my_form.date_to and my_form.date_to > my_form.date_from :
                    my_form.save()
                    date_to = my_form.date_to 
                    date_from= my_form.date_from 
                    unit = my_form.unit
                    create =  timezone.now().date()
                    context = {
                        'date_to':date_to,
                        'date_from':date_from,
                        'unit':unit,
                        'create':create
                    }
                    return render(request,'unit/available.html',context)
                else:
                    not_valid1 = 'Not valid date, Please check the date you entered and try again '
                    return render(request,'unit/not_available.html',{'not1':not_valid1} )
            else:
                not_valid2 = unit.book_unit.aggregate(book_ends_is=Max("date_to"))
                return render(request,'unit/not_available.html',{'not2':not_valid2} )

            
    else:
         form = UnitBookForm() 
         
    context = {"unit":unit,'form':form}
    return render(request,'unit/unit_detail.html',context)

