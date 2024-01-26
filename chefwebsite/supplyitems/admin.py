from django.contrib import admin

# Register your models here.
from .models import SupplyItem, SupplyItemAdmin

admin.site.register(SupplyItem, SupplyItemAdmin)