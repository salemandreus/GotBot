from django.shortcuts import render

from chefsite.views import ItemListBase
from .models import Stock

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
                qs = Stock.objects.select_related()

            return qs

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
                qs = Stock.objects.all()

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
                qs = Stock.objects.all()

            return qs

        qs = query_items()
        context['objects_count'] = qs.count()
        # Add Pagination
        context['page_obj'] = self.paginate(qs, 30, request)

        return render(request, template_name, context)




def update(request):
    return render(request, 'stock/form.html', {})

def confirm_update(request):
    return render(request, 'stock/confirm-update.html', {})

