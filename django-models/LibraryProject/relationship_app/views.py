from django.shortcuts import render
from django.views.generic import DetailView
from .models import Author, Book, Library, Librarian
# Create your views here.


def book_list(request):
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