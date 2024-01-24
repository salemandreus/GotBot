from django.urls import path
from supplyitems import views

urlpatterns = [
    path('', views.SupplyItemListPage.as_view(), name='list_supplyitems'),
]