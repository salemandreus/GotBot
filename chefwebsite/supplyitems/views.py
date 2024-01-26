from django.shortcuts import render, redirect, get_object_or_404

from chefsite.views import ItemListBase

from .forms import SupplyItemModelForm

from .models import SupplyItem


class SupplyItemListPage(ItemListBase):
    """
    Return List of SupplyItem. Todo:Include links to Detailed supplyitem.
    """
    def get(self, request):
        template_name = "supplyitems/supplyitems-list.html"
        # context = {"utc_now": datetime.now(timezone.utc)}
        context = {
            "name": "Supply Items",
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


def detail(request):
    return render(request, 'supplyitems/detail.html', {})


def create(request):
    """ Create SupplyItem via a form. """

    template_name = "supplyitems/form.html"

    context = {"title": "Create A New SupplyItem"}
    form = SupplyItemModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.last_edited_by = request.user

        # obj.name= form.cleaned_data.get("name") + "0"
        obj.save()

        # return redirect("detail_supplyitem", obj.slug)
        return redirect("list_supplyitems")
    context["form"] = form


    # todo: creating triggers adding initial stock item and prompt whether to add stock, default to 0 otherwise

    return render(request, template_name, context)

def update(request, slug):
    """ Update existing SupplyItem via a form. """

    obj = get_object_or_404(SupplyItem, slug=slug)
    if obj is None: # todo: test
        return redirect("list_supplyitems")
    else:
        context = {"title": f"Update {obj.name}"}
        # GET EXISTING FORM
        form = SupplyItemModelForm(request.POST or None, request.FILES or None, instance=obj)
        if form.is_valid():
            form.save()

            # return redirect("detail_supplyitem", obj.slug)  # args=form.fields.slug))
            return redirect("list_supplyitems")  # args=form.fields.slug))

        context["form"] = form
    template_name = "supplyitems/form.html"

    return render(request, template_name, context)


def delete(request):
    return render(request, 'supplyitems/delete.html', {})