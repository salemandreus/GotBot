from django.conf import settings
from django.db import models
from django.contrib import admin
from django.urls import reverse

User = settings.AUTH_USER_MODEL

class SupplyItem(models.Model):
    code = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    notes = models.TextField(help_text="Notes about product stock management of this item.", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)                                                      # no backward relation
    last_edited_by = models.ForeignKey(User, on_delete=models.PROTECT)    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+",)
    min_amount = models.IntegerField(help_text="Below this amount, stock is 'low'", default=0)
    med_amount = models.IntegerField(help_text="Below this amount, stock is at 'medium' amount", default=0)
    max_amount = models.IntegerField(help_text="At this amount, stock is at 'max recommended', above it is 'above max recommended'", default=0)

    def get_absolute_url(self):
        return f"{reverse('list_supplyitems')}{self.slug}"

    def get_edit_url(self):
        return f"{self.get_absolute_url()}/edit"

    def get_delete_url(self):
        return f"{self.get_absolute_url()}/delete"

    def get_stock_item_url(self):
        return f"{reverse('list_stock')}{self.slug}"

class SupplyItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("code",)}
