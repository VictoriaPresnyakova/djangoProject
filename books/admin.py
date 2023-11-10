from django.contrib import admin
from .models import Book, Genre, Review, Author, Character

admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Review)
admin.site.register(Author)
admin.site.register(Character)