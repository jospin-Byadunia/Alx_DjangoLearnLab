from .views import LibraryDetailView
from django.urls import path, include
from django.contrib import admin
from .views import list_books
from .views import login_view
from .views import logout_view
from .views import signup_view


urlpatterns = [
    path('book-list/', list_books, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signup/', signup_view, name='signup'),
]