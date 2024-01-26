from django.shortcuts import render, get_object_or_404

from chefsite.views import ItemListBase
from .models import SupplyItem
from django.db.models import F

#todo: make a stock and supplies base
class StockLowListPage(ItemListBase):
    """
    Return List of Stock Items. Todo: Include links to Detailed stock items.
    """
    def get(self, request):
        template_name = "chefsite/list-page.html"
        # context = {"utc_now": datetime.now(timezone.utc)}
        context = {
            "title": "Stock Running Low",
            "card_type": "stock",
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
        template_name = "chefsite/list-page.html"
        # context = {"utc_now": datetime.now(timezone.utc)}
        context = {
            "title": "Stock Recently Refilled",
            "card_type": "stock",
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
        template_name = "chefsite/list-page.html"
        # context = {"utc_now": datetime.now(timezone.utc)}
        context = {
            "title": "All Stock",
            "card_type": "stock",
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


def detail(request, slug):
    """
    Retrieve a single item with its stock amount via a slug (detailed).
    Include buttons to update stock amount.
    """
    template_name = "chefsite/detail.html"
    obj = get_object_or_404(SupplyItem, slug=slug)
    context = {
        "title": f"Code: {obj.code} Name: {obj.name}",
        "card_type": "stock",
        "object": obj
    }

    return render(request, template_name, context)

def update(request):
    return render(request, 'stock/form.html', {})

def confirm_update(request):
    return render(request, 'stock/confirm-update.html', {})

