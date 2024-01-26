from django.urls import path
from supplyitems import views

urlpatterns = [
    path('', views.SupplyItemListPage.as_view(), name='list_supplyitems'),
    path('<str:slug>/edit/', views.update, name='update_supplyitem'),
    path('<str:slug>/delete/', views.delete, name='delete_supplyitem'),
    # path('detail/', views.detail, name='detail_supplyitem'),
]