from django.shortcuts import render

from chefsite.views import ItemListBase
from .models import SupplyItem


class SupplyItemListPage(ItemListBase):
    """
    Return List of SupplyItem. Todo:Include links to Detailed supplyitem.
    """
    def get(self, request):
        template_name = "supplyitems/supplyitems-list.html"
        # context = {"utc_now": datetime.now(timezone.utc)}
        context = {
            "title": "Supply Items",
        }

        # get stock
        def query_items():
            if request.user.is_authenticated:
                qs = SupplyItem.objects.select_related()

            return qs

        qs = query_items()
        context['objects_count'] = qs.count()
        # Add Pagination
        context['page_obj'] = self.paginate(qs, request)

        return render(request, template_name, context)



def detail(request):
    return render(request, 'supplyitems/detail.html', {})

def create(request):
    return render(request, 'supplyitems/create.html', {})

def update(request):
    return render(request, 'supplyitems/update.html', {})

def delete(request):
    return render(request, 'supplyitems/delete.html', {})