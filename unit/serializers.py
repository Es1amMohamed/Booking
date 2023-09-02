from rest_framework import serializers
from .models import *
from .booking_func.availability import *
from django.db.models import Max

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitBook
        fields = ["unit",'date_from','date_to','adults','children']
