from django.shortcuts import render
from django.core.paginator import Paginator
from unit.models import *

# Create your views here.


def home(request):
    
    units = Unit.objects.all()
    paginator = Paginator(units,1)
    page = request.GET.get('page')
    page_ogj = paginator.get_page(page)
    context = {'units':page_ogj}
    
    return render(request, 'settings/home.html' ,context)


def services(request):
    
    
    return render(request, 'settings/services.html')


def about_us(request):
    
    units = Unit.objects.all()
    context = {'units':units}

    return render(request,'settings/about_us.html', context)



def contact(request):
    
    
    return render(request,'settings/contact.html')