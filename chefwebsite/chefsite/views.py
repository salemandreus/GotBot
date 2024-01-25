from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View

from supplyitems.models import SupplyItem
from django.db.models import F


class ItemListBase(View):
    """Will be inherited and overridden by other views that list items."""
    def paginate(self, item_list, per_page, request):
        """paginate a list of items. The number per page is passed in as per_page."""
        paginator = Paginator(item_list, per_page)
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
                low_stock = SupplyItem.objects.filter(min_amount__gt=F("stock__amount")).select_related()
                stock = SupplyItem.objects.select_related()
                supplyitems = SupplyItem.objects.all()

            return low_stock, stock, supplyitems

        low_stock, stock, supplyitems = query_items()
        context['low_stock_objects_count'] = low_stock.count()
        context['stock_objects_count'] = stock.count()
        context['supplyitems_objects_count'] = supplyitems.count()
        # Add Pagination
        context['page_obj_low_stock'] = self.paginate(low_stock, 5, request)  # todo: calculate based on size of screen then pass in that value
        context['page_obj_stock'] = self.paginate(stock, 5, request)
        context['page_obj_supplyitems'] = self.paginate(supplyitems, 5, request)

        return render(request, template_name, context)
