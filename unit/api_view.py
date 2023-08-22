from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import *

class UnitAPIList(ListCreateAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    
    
    
class UnitAPIdetail(RetrieveUpdateDestroyAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer