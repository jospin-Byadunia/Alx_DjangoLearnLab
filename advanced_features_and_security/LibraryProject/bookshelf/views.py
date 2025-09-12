from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout
from .models import Book
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required

# Create your views here.

def bookl_list_view(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book_view(request):
    return render(request, "bookshelf/edit_book.html")

@permission_required('bookshelf.can_add', raise_exception=True)
def add_book_view(request):
    return render(request, "bookshelf/add_book.html")
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book_view(request):
    return render(request, "bookshelf/delete_book.html")

def view_book_view(request):
    return render(request, "bookshelf/view_book.html") 

def search_books(request):
    query = request.GET.get("q", "")
    # ORM automatically parameterizes queries to prevent SQL injection
    books = Book.objects.filter(title__icontains=query)
    return render(request, "bookshelf/view_book.html", {"books": books}) 