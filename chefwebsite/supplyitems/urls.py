from django.urls import path
from supplyitems import views

urlpatterns = [
    path('', views.list, name='list_supplyitems'),
]