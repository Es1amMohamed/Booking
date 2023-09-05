from .models import *
from .serializers import ProfileSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import (
    api_view,
)


@login_required
@api_view(["GET"])
def api_profile(request):
    profile = get_object_or_404(User, username=request.user)
    data = ProfileSerializer(profile, context={"request": request}).data
    return Response({"data": data})
