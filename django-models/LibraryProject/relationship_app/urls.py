from .views import book_list, LibraryDetailView
from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('book-list/', book_list, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]