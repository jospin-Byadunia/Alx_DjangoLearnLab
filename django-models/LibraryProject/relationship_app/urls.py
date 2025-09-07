from .views import LibraryDetailView
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books
import views


urlpatterns = [
    path('book-list/', list_books, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path("register/", views.register, name="register"),   # <-- match the view name
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("admin/", include("relationship_app.admin_view")),
    path("librarian/", include("relationship_app.librarian_view")),
    path("member/", include("relationship_app.member_view")),
    path("add-book/", include("relationship_app.add_book_view")),
    path("edit-book/", include("relationship_app.change_book_view")),
    path("delete-book/", include("relationship_app.delete_book_view")),
]

#views.register