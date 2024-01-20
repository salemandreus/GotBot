from django.urls import path
from stock import views

urlpatterns = [
    path('', views.list, name='list_stock'),
]