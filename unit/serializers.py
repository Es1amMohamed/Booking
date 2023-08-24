from rest_framework import serializers
from .models import *


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitBook
        exclude = ["id", "user"]
