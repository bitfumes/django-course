from django.shortcuts import render
from books.models import Book


def index(request):
    dbData = Book.objects.all()
    context = {'books': dbData}
    return render(request, 'books/index.html', context)


def show(request, id):
    singleBook = Book.objects.get(pk=id)
    context = {'book': singleBook}
    return render(request, 'books/show.html', context)
