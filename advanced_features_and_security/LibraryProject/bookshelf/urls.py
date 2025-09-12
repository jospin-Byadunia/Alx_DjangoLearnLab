from django.urls import path
from . import views

urlpatterns = [
    path('view-book/', views.view_book_view, name='view_book'),
    path('edit-book/', views.edit_book_view, name='edit_book'),
    path('add-book/', views.add_book_view, name='add_book'),
    path('delete-book/', views.delete_book_view, name='delete_book'),
    ]