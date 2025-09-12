from models import Author, Book, Library, Librarian

# Sample Queries
# authors = Author.objects.all()
# books = Book.objects.all()
# library = Library.objects.get(name='library_name')
# books = library.books.all()
# librarians = Librarian.objects.all()
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

def get_librarian_by_library(library_name):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)