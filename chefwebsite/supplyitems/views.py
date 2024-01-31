from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect, get_object_or_404

from chefsite.views import ItemListBase
from stock.models import Stock

from .forms import SupplyItemModelForm

from .models import SupplyItem


class SupplyItemListPage(ItemListBase):
    """
    Displays List of SupplyItems.
    """

    def get_context_data(self):
        context = super().get_context_data()
        context["card_type"] = "supplyitem"
        context["title"] = "Supply Items"

        return context


def detail(request, slug):
    """
    Displays a single supplyitem via a slug (detailed).
    """

    template_name = "chefsite/detail-page.html"
    obj = get_object_or_404(SupplyItem, slug=slug)
    context = {
        "title": f"Code: {obj.code} Name: {obj.name}",
        "card_type": "supplyitem",
        "object": obj
    }

    return render(request, template_name, context)


def create(request):
    """ Create SupplyItem via a form. """

    template_name = "supplyitems/form.html"

    context = {"title": "Create A New SupplyItem"}
    if request.user.is_authenticated:
        form = SupplyItemModelForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.last_edited_by = request.user
            obj.save()

            # Created a Stock record that corresponds to the SupplyItem
            stock_item = Stock(item_code=obj, amount=0, refilled_by=request.user)
            stock_item.save()
                                                                                                    # obj.name= form.cleaned_data.get("name") + "0"
            # Redirect to Stock Detail Page for created item                                                 #todo: redirects to detailed vs list as appropriate - change again if Modal
            return redirect("detail_stock", obj.slug)                       # todo: a notification on how they can add stock
                                                                                   # todo: redirect to add-stock form view! with a skip option redirects to list or item
    context["form"] = form

    # todo: creating triggers adding initial stock item and prompt whether to add stock, default to 0 otherwise

    return render(request, template_name, context)

@staff_member_required
def update(request, slug):
    """ Update existing SupplyItem via a form. """

    template_name = "supplyitems/form.html"
    context = {}
    # if request.user.is_authenticated: Todo: does it return this if unauthorized? Test
    obj = get_object_or_404(SupplyItem, slug=slug)
    if obj is None: # todo: test
        return redirect("list_supplyitems")
    else:
        context ["title"] = f"Update {obj.name}"
        # GET EXISTING FORM
        form = SupplyItemModelForm(request.POST or None, request.FILES or None, instance=obj)
        if form.is_valid():
            form.save()

            # return redirect("detail_supplyitem", obj.slug)  # args=form.fields.slug))
            return redirect("list_supplyitems")  # args=form.fields.slug))

        context["form"] = form

    return render(request, template_name, context)


@staff_member_required
def delete(request, slug):
    """Delete SupplyItem. Only staff members are allowed to do this.""" # todo: make sure this works with staff only

    template_name = "supplyitems/confirm-delete.html"
    context = {}
    if request.user.is_authenticated:
        obj = get_object_or_404(SupplyItem, slug=slug)

        if request.method == "POST":
            if request.POST.get("cancel"):
                return redirect('list_supplyitems')
            elif request.POST.get("confirm"):
                obj.delete()
                return redirect("list_supplyitems")

        context["object"] = obj

    return render(request, template_name, context)
