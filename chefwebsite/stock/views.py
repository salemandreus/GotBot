from django.shortcuts import render

from chefsite.views import ItemListBase
from .models import Stock

class StockListPage(ItemListBase):
    """
    Return List of Stock Items. Todo: Include links to Detailed stock items.
    """
    def get(self, request):
        template_name = "stock/list.html"
        # context = {"utc_now": datetime.now(timezone.utc)}
        context = {
            "title": "Stock Available",
        }

        # get stock
        def query_items():
            if request.user.is_authenticated:
                qs = Stock.objects.all()

            return qs

        qs = query_items()
        context['objects_count'] = qs.count()
        # Add Pagination
        context['page_obj'] = self.paginate(qs, request)

        return render(request, template_name, context)




def update(request):
    return render(request, 'stock/form.html', {})

def confirm_update(request):
    return render(request, 'stock/confirm-update.html', {})

