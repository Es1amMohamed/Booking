from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *

# Register your models here.


class SomeModelAdmin(SummernoteModelAdmin):
    summernote_fields = "__all__"


admin.site.register(Unit, SomeModelAdmin)
admin.site.register(Category)
admin.site.register(Place)
admin.site.register(UnitBook)
