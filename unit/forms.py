from typing import Any, Dict, Mapping, Optional, Type, Union
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import *


class UnitBookForm(forms.ModelForm):
    class Meta:
        model = UnitBook
        fields = ["date_from", "date_to", "adults", "children"]

        widgets = {
            "date_from": forms.DateInput(attrs={"type": "date"}),
            "date_to": forms.DateInput(attrs={"type": "date"}),
        }
