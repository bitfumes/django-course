from django.shortcuts import render


def index(request):
    context = {'name': 'Sarthak'}
    return render(request, 'books/index.html', context)
