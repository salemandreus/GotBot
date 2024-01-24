from django.urls import path
from stock import views

urlpatterns = [
    path('', views.StockAllListPage.as_view(), name='list_stock'),
    path('running-low/', views.StockLowListPage.as_view(), name='list_stock_low'),
    path('refilled/', views.StockRefilledListPage.as_view(), name='list_stock_refilled'),
]