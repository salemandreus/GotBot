from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


# Create your models here.
class SupplyItems(models.Model):
    code = models.CharField(max_length=15, primary_key=True)
    name = models.CharField(max_length=255)
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)                                                      # no backward relation
    # edited_by = models.ForeignKey(User, default=1, null=True, on_delete=models.PROTECT)    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+",)
