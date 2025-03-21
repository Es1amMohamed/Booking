from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import *

# Create your views here.


def post_list(request):
    posts = Post.objects.all()

    return render(request, "blog/post_list.html", {"posts": posts})

def post_list_apis(request):
    return render(request, "blog/post_list_api.html")


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post_detail.html", {"post": post})
