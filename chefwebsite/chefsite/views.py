from django.shortcuts import render


def home(request):
    context = {
        "title": "Welcome back, {username}!".format(username=request.user),
    }

    return render(request, 'index.html', context)