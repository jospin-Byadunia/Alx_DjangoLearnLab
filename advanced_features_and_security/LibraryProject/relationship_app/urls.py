from .views import LibraryDetailView
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books
from . import views
from relationship_app.views import Register 


urlpatterns = [
    path('book-list/', list_books, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path("register/", Register.as_view(), name="register"), 
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("admin/", views.admin_view, name="admin_view"),
    path("librarian/", views.librarian_view, name="librarian_view"),
    path("member/", views.member_view, name="member_view"),
    path("add_book/", views.add_book_view, name="add_book"),
    path("edit_book/", views.change_book_view, name="change_book"),
    path("delete-book/", views.delete_book_view, name="delete_book"),
]

#views.register