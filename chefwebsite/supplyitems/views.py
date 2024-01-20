from django.shortcuts import render

def list(request):
    context = {
        "title": "Supply Items",
    }

    return render(request, 'list.html', context)

def detail(request):
    return render(request, 'detail.html', {})

def create(request):
    return render(request, 'create.html', {})

def update(request):
    return render(request, 'update.html', {})

def delete(request):
    return render(request, 'delete.html', {})