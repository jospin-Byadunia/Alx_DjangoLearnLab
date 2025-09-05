from .views import LibraryDetailView
from django.urls import path, include
from django.contrib import admin
from .views import list_books


urlpatterns = [
    path('book-list/', list_books, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]