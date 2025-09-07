from .views import LibraryDetailView
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books
import views


urlpatterns = [
    path('book-list/', list_books, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path("register/", views.register, name="register"),   # <-- match the view name
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]