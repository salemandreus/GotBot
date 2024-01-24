from django.conf import settings
from django.db import models
# from django.contrib import admin

User = settings.AUTH_USER_MODEL

# Create your models here.
class SupplyItem(models.Model):
    code = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)                                                      # no backward relation
    last_edited_by = models.ForeignKey(User, on_delete=models.PROTECT)    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+",)
    min_amount = models.IntegerField(help_text="Below this amount, stock is 'low'")
    med_amount = models.IntegerField(help_text="Below this amount, stock is at 'medium' amount")
    max_amount = models.IntegerField(help_text="At this amount, stock is at 'max recommended', above it is 'above max recommended'")

