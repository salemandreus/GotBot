from django.shortcuts import render

from chefsite.views import ItemListBase
from .models import SupplyItem
from django.db.models import F

#todo: make a stock and supplies base
class StockLowListPage(ItemListBase):
    """
    Return List of Stock Items. Todo: Include links to Detailed stock items.
    """
    def get(self, request):
        template_name = "stock/running-low-list.html"
        # context = {"utc_now": datetime.now(timezone.utc)}
        context = {
            "title": "Stock Running Low",
        }

        # get stock
        def query_items():
            if request.user.is_authenticated:
                low_stock = SupplyItem.objects.filter(min_amount__gt=F("stock__amount")).select_related()

            return low_stock

        qs = query_items()
        context['objects_count'] = qs.count()

        # Add Pagination
        context['page_obj'] = self.paginate(qs, 30, request)

        return render(request, template_name, context)


class StockRefilledListPage(ItemListBase):
    """
    Return List of Stock Items. Todo: Include links to Detailed stock items.
    """
    def get(self, request):
        template_name = "stock/recently-refilled-list.html"
        # context = {"utc_now": datetime.now(timezone.utc)}
        context = {
            "title": "Stock Recently Refilled",
        }

        # get stock
        def query_items():
            if request.user.is_authenticated:
                qs = SupplyItem.objects.select_related()

            return qs

        qs = query_items()
        context['objects_count'] = qs.count()
        # Add Pagination
        context['page_obj'] = self.paginate(qs, 30, request)

        return render(request, template_name, context)


class StockAllListPage(ItemListBase):
    """
    Return List of Stock Items. Todo: Include links to Detailed stock items.
    """
    def get(self, request):
        template_name = "stock/all-list.html"
        # context = {"utc_now": datetime.now(timezone.utc)}
        context = {
            "title": "All Stock",
        }

        # get stock
        def query_items():
            if request.user.is_authenticated:
                qs = SupplyItem.objects.select_related()

            return qs

        qs = query_items()
        context['objects_count'] = qs.count()
        # Add Pagination
        context['page_obj'] = self.paginate(qs, 30, request)

        return render(request, template_name, context)



# class StockDetailPage(ItemListBase):#Todo: make a ItemDetailBase
#     """
#     Retrieve a single stock item via a slug (detailed).
#     Include buttons to add/edit stock amounts.

#     """
#     def get(self, request, slug):
#         obj = get_object_or_404(Stock, slug=slug)
#         template_name = "stock/detail.html"
#
#         def query_stock():
#             # Get item with stock amount
#             qs = obj.responses().published()
#             if request.user.is_authenticated:
#                 my_qs = obj.responses().filter(user=request.user)
#                 qs = (qs | my_qs).distinct()
#             return qs
#
#         qs = query_stock()
#
#         return render(request, template_name, context)


def update(request):
    return render(request, 'stock/form.html', {})

def confirm_update(request):
    return render(request, 'stock/confirm-update.html', {})

