from django.db import models
from supplyitems.models import SupplyItems


# from ..supplyitems.models import SupplyItems

# Create your models here.
class Stock(models.Model):
    item_code = models.ForeignKey(SupplyItems, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)