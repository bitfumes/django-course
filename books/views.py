from django.shortcuts import render, get_object_or_404, redirect
from books.models import Book, Review
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


class BookListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return Book.objects.all()


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = context['book'].review_set.order_by('-created_at')
        context['authors'] = context['book'].authors.all()
        return context


def author(request, author):
    books = Book.objects.filter(authors__name=author)
    context = {'book_list': books}
    return render(request, 'books/book_list.html', context)


def review(request, id):
    body = request.POST['review']
    newReview = Review(body=body, book_id=id)
    newReview.save()
    return redirect('/book')
