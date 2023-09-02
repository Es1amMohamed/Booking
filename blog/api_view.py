from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def post_list_api(request):
    all_posts = Post.objects.all()
    data = PostSerializer(all_posts, many=True, context={"request": request}).data

    return Response({"data": data})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def post_detail_api(request, id):
    post_detail = get_object_or_404(Post, id=id)
    data = PostSerializer(post_detail, context={"request": request}).data

    return Response({"data": data})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def post_search_api(request, query):
    posts = Post.objects.filter(
        Q(title__icontains=query) | Q(residency_programme__icontains=query)
    )
    data = PostSerializer(posts, many=True).data

    return Response({"data": data})
