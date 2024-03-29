from django.urls import path
from stock import views

urlpatterns = [
    path('', views.StockAllListPage.as_view(), name='list_stock'),
    path('running-low/', views.StockLowListPage.as_view(), name='list_stock_low'),
    path('out-of-stock/', views.StockEmptyListPage.as_view(), name='list_stock_empty'),
    path('refilled/', views.StockRefilledListPage.as_view(), name='list_stock_refilled'),# WIP therefore not on nav
    path("<str:slug>/", views.detail, name='detail_stock'),
    path("<str:slug>/update/", views.StockUpdate.as_view(), name='update_stock'),
]