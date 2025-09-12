from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout
from .models import Book
from .models import Library
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy    
from django.views.generic import CreateView
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required

# Create your views here.


def list_books(request):
    books = Book.objects.all()  # Optimized query
    return render(request, "relationship_app/list_books.html", {"books": books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add all books in this library
        context["books"] = self.object.books.all()
        return context

class Register(CreateView):
    form_class = UserCreationForm()
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Django's login function
            return redirect("book_list")
    else:
        form = AuthenticationForm()


# --- Logout View ---
def logout_view(request):
    logout(request)  # Django’s logout
    return render(request, "relationship_app/logout.html")
    # views.register
# LibraryDetailView
# admin_view

def is_admin(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "admin"

@user_passes_test(is_admin, login_url="/login/")
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

# librarian_view
def is_librarian(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "librarian"

@user_passes_test(is_librarian, login_url="/login/")
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

# member_view
def is_member(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "member"

@user_passes_test(is_member, login_url="/login/")
def member_view(request):
    return render(request, "relationship_app/member_view.html")

# Add Book View
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book_view(request):
    return render(request, 'relationship_app/add_book.html')


# change book view
@permission_required('relationship_app.can_change_book', raise_exception=True)
def change_book_view(request):
    return render(request, 'relationship_app/change_book.html')

# delete book view
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book_view(request):
    return render(request, 'relationship_app/delete_book.html')