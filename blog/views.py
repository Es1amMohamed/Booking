from django.shortcuts import render
from .models import  *
# Create your views here.


def post_list(request):
    return render(request,'blog/post_list.html')


def post_detail(request,slug):
    pass