from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View

from supplyitems.models import SupplyItem
from stock.models import Stock


class ItemListBase(View):
    """Will be inherited and overridden by other views that list items."""
    def paginate(self, item_list, request):
        """paginate a list of items"""
        paginator = Paginator(item_list, 15)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return page_obj

    def get(self, request):
        """Base Get Functionality for a ItemList class to be overridden."""
        template_name = ""
        context = {}
        return render(request, template_name, context)


# Todo: Detailed Base


class HomePage(ItemListBase):
    """
    Return List of Items. Todo:Include links to Detailed item.
    """
    def get(self, request):
        template_name = "chefsite/index.html"
        # context = {"utc_now": datetime.now(timezone.utc)}
        context = {
            "title": "Welcome back, {username}!".format(username=request.user),
        }

        # get stock
        def query_items():
            # Todo: get only items running low
            if request.user.is_authenticated:
                stock = Stock.objects.all()
                supplyitems = SupplyItem.objects.all()

            return stock, supplyitems

        stock, supplyitems = query_items()
        context['stock_objects_count'] = stock.count()
        context['supplyitems_objects_count'] = supplyitems.count()
        # Add Pagination
        # context['page_obj'] = self.paginate(qs, request)

        return render(request, template_name, context)
