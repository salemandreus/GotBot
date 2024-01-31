from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from chefsite.views import ItemListBase
from .models import SupplyItem, Stock
from django.db.models import F

from .forms import StockModelForm

class StockListBase(ItemListBase):
    """
    Overrides ItemListBase. Inherited by all Stock Lists.
    """

    def get_context_data(self):
        context = super().get_context_data()
        context["card_type"] = "stock"

        return context

    # def get(self, request):
    #     super().get(request)


class StockEmptyListPage(StockListBase):
    """
    Displays a List of Out Of Stock Items.
    """

    def query_items(self, request):
        if request.user.is_authenticated:
            empty_stock = SupplyItem.objects.filter(stock__amount=0).select_related()

        return empty_stock

    def get_context_data(self):
        context = super().get_context_data()
        context["title"] = "Out Of Stock"

        return context


class StockLowListPage(StockListBase):
    """
    Displays List of the Stock Items that are running low.
    """

    def query_items(self, request):
        if request.user.is_authenticated:
            low_stock = (SupplyItem.objects.filter(min_amount__gt=F("stock__amount"))
                         .filter(stock__amount__gt=0).select_related())
        return low_stock

    def get_context_data(self):
        context = super().get_context_data()
        context["title"] = "Stock Running Low"

        return context


class StockRefilledListPage(StockListBase):
    """
    Display List of Recently Refilled Stock Items.     # WIP - not currently linked
    """

    def get_context_data(self):
        context = super().get_context_data()
        context["title"] = "Stock Recently Refilled"
        return context


class StockAllListPage(StockListBase):
    """
    Display List of All stock items.
    """

    def get_context_data(self):
        context = super().get_context_data()
        context["title"] = "All Stock"

        return context


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


#Todo: LoginRequiredMixin
class StockUpdate(View):
    """
    Update stock amount.
    """
    def get_context_data(self):
        context = {
            "card_type" : "stock",
        }
        return context

    def get_form(self, request, slug):
        """Get Simple Form To Update Stock Amount"""
        code = SupplyItem.objects.filter(slug=slug).first().code
        obj = get_object_or_404(Stock, item_code=code)
        form = StockModelForm(request.POST or None, request.FILES or None, instance=obj)
        return code, obj, form

    def post_form(self, request, slug):
        """Post Simple Form To Update Stock Amount"""
        code = SupplyItem.objects.filter(slug=slug).first().code
        obj = get_object_or_404(Stock, item_code=code)
        form = StockModelForm(request.POST or None, request.FILES or None, instance=obj)
        if form.is_valid():
            form.save()

    def get(self, request, slug):
        context = self.get_context_data()

        if context["card_type"] == "stock":
            code, obj, form = self.get_form(request, slug)
            context["form"] = form

        template_name = 'stock/form.html'
        # context["title"] = "Update Stock"
        # context["subtitle"] = f"Code: {code} Name: {obj.item_code.name}"

        # if obj is None:
        #     return redirect("list_stock")

        return render(request, template_name, context)

    def post(self, request, slug):
        context = self.get_context_data()
        # if context["card_type"] == "stock":
        self.post_form(request, slug)

        # return redirect("list_stock")
        return redirect("detail_stock", slug)
