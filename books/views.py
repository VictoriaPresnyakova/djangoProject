from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Book, Character


class BooksView(ListView):
    """Books List"""
    model = Book
    queryset = Book.objects.filter(draft=False)
    # template_name = 'books/book_list.html'


class BookInfoView(DetailView):
    """Book Info"""
    model = Book
    slug_field = 'url'
    # template_name = 'books/book_detail.html'


class CharacterFilteredView(View):
    """Character Filtered"""

    def get(self, request, slug):
        book = Book.objects.get(url=slug)
        characters = book.characters.all()
        return render(request, 'characters/../templates/books/character_list.html', {'character_list': characters,
                                                                  'book_title': book.title})


class CharacterInfoView(DetailView):
    """Character Info"""
    model = Character
    slug_field = 'url'
