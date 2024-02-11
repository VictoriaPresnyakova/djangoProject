from django.urls import path
from . import views


urlpatterns = [
    path('books', views.BooksView.as_view()),
    path('', views.BooksView.as_view()),
    path('book/<slug:slug>/', views.BookInfoView.as_view(), name='book_info'),
    path('characters/<slug:slug>/', views.CharacterFilteredView.as_view(), name='character_filtered'),
    path('character/<slug:slug>/', views.CharacterInfoView.as_view(), name='character_info')

]