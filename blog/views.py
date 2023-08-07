from django.shortcuts import render
from .models import  *
# Create your views here.


def post_list(request):
    
    posts = Post.objects.all()
    
    
    return render(request,'blog/post_list.html', {'posts':posts })


def post_detail(request,slug):
    post = Post.objects.get(slug=slug)    
    return render(request,'blog/post_detail.html',{'post':post})
