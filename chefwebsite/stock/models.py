from django.conf import settings
from django.db import models

from supplyitems.models import SupplyItem

User = settings.AUTH_USER_MODEL


class Stock(models.Model):
    item_code = models.OneToOneField(SupplyItem, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    refilled = models.DateTimeField(auto_now=True)                                                      # no backward relation
    refilled_by = models.ForeignKey(User, on_delete=models.PROTECT)
