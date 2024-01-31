from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View

from supplyitems.models import SupplyItem
from django.db.models import F


class ItemListBase(View):
    """Base functionality for all lists, will be inherited and overridden by other views that list stock and supply items."""

    def query_items(self, request):
        """
        Get supplyitems and related stock
        """
        if request.user.is_authenticated:
            qs = SupplyItem.objects.select_related()
        return qs

    def get_context_data(self):
        """
        Override with and return the view-specific context data defined as a dictionary called "context".
        """
        context = {
            "title": "",# Page Title
            "card_type": "", # "stock" or "supplyitem"
            "card_tooltip_message": "" # use the stock message or the supplyitem message
        }
        return context

    def paginate(self, item_list, per_page, request):
        """
        Paginate a list of items. The number per page is passed in as per_page.
        """
        paginator = Paginator(item_list, per_page)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        return page_obj

    def get(self, request):
        """
        Base Get Functionality for a ItemList class to be overridden.
        """
        template_name = ""
        context = {}
        return render(request, template_name, context)


class HomePage(ItemListBase):
    """
    Return List of Items.
    """

    def query_items(self, request):
        if request.user.is_authenticated:
            low_stock = (SupplyItem.objects.filter(min_amount__gt=F("stock__amount"))
                         .filter(stock__amount__gt=0).select_related())
            out_of_stock = SupplyItem.objects.filter(stock__amount=0).select_related()
            # refilled = SupplyItem.objects.select_related() # wip filter refilled
            supplyitems = SupplyItem.objects.all()

        return low_stock, out_of_stock, supplyitems  # ,refilled

    def get_context_data(self):
        context = {
            "title": "Welcome back, {username}!".format(username=request.user),
            "supplyitems_card_tooltip_message" : "Click to view full info for the supply item.",
            "stock_card_tooltip_message" : "Click to view full info or update stock."
        }
        return context

    def get(self, request):
        template_name = "chefsite/index.html"
        context = self.get_context_data()

        # get all supplyitems and stock lists that are on home page
        low_stock, out_of_stock, supplyitems = self.query_items(request)     #wip refilled

        # Append lists to context
        context['low_stock_objects_count'] = low_stock.count()
        context['out_of_stock_objects_count'] = out_of_stock.count()
        # context['refilled_stock_objects_count'] = refilled.count()
        context['supplyitems_objects_count'] = supplyitems.count()

        # Add Pagination
        context['page_obj_low_stock'] = self.paginate(low_stock, 5, request)  # todo: calculate based on size of screen then pass in that value
        context['page_obj_out_of_stock'] = self.paginate(out_of_stock, 5, request)  # todo: calculate based on size of screen then pass in that value
        # context['page_obj_refilled_stock'] = self.paginate(refilled, 5, request)
        context['page_obj_supplyitems'] = self.paginate(supplyitems, 5, request)

        return render(request, template_name, context)
