from django import forms
from .models import *
class UnitBookForm(forms.ModelForm):
    class Meta:
            model = UnitBook
            fields = ['date_from','date_to','adults','children']
            