from django.shortcuts import render
from django.views import View

from .models import Book


class BooksView(View):
    """Books List"""
    def get(self, request):
        books = Book.objects.all()
        return render(request, 'books/book_list.html', {'book_list': books})
