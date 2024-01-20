from django.shortcuts import render

# Create your views here.
def list(request):
    context = {
        "title": "Stock Available",
    }

    return render(request, 'list.html', context)

def update(request):
    return render(request, 'form.html', {})

def confirm_update(request):
    return render(request, 'confirm-update.html', {})

