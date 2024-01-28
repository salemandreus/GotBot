from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect

from chefsite.views import ItemListBase
from .models import SupplyItem, Stock
from django.db.models import F

from .forms import StockModelForm

#todo: make a stock and supplies base
class StockEmptyListPage(ItemListBase):
    """
    Return List of Stock Items. Todo: Include links to Detailed stock items.
    """
    def get(self, request):
        template_name = "chefsite/list-page.html"
        # context = {"utc_now": datetime.now(timezone.utc)}
        context = {
            "title": "Out Of Stock",
            "card_type": "stock",
            "card_tooltip_message": "Click to view full info or update stock.",
        }

        # get stock
        def query_items():
            if request.user.is_authenticated:
                low_stock = SupplyItem.objects.filter(stock__amount=0).select_related()

            return low_stock

        qs = query_items()
        context['objects_count'] = qs.count()

        # Add Pagination
        context['page_obj'] = self.paginate(qs, 30, request)

        return render(request, template_name, context)


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
            "card_tooltip_message": "Click to view full info or update stock.",
        }

        # get stock
        def query_items():
            if request.user.is_authenticated:
                low_stock = (SupplyItem.objects.filter(min_amount__gt=F("stock__amount"))
                                                .filter(stock__amount__gt=0).select_related())

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
            "card_tooltip_message": "Click to view full info or update stock."
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
            "card_tooltip_message": "Click to view full info or update stock."
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
    template_name = "chefsite/detail-page.html"
    obj = get_object_or_404(SupplyItem, slug=slug)
    context = {
        "title": f"Code: {obj.code} Name: {obj.name}",
        "card_type": "stock",
        "object": obj
    }

    return render(request, template_name, context)


@staff_member_required
def update(request, slug):
    """
    Update stock amount.
    """
    context = {}
    template_name = 'stock/form.html'

    # if request.user.is_authenticated: Todo: does it return this if unauthorized? Test

    # Get the SupplyItem code that pertains to our supplyitem and its stock object
    code = SupplyItem.objects.filter(slug=slug).first().code
    # Get the relevant Stock object to have its amount updated in the form
    obj = get_object_or_404(Stock, item_code=code)
    if obj is None:  # todo: test - this shouldn't happen as we're getting the slug from its own detail page
        return redirect("list_stock") # todo: use referring page, whichever it was
    else:
        context["title"] = f"Update Stock"
        context["subtitle"] = f"Code: {code} Name: {obj.item_code.name}"
        # GET EXISTING FORM
        form = StockModelForm(request.POST or None, request.FILES or None, instance=obj)
        if form.is_valid():
            form.save()

            # return redirect("detail_supplyitem", obj.slug)  # args=form.fields.slug))
            return redirect("detail_stock", obj.item_code.slug)  # args=form.fields.slug))

        context["form"] = form

    return render(request, template_name, context)
