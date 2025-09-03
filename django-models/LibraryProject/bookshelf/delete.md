from bookshelf.models import Book

# Delete the book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion by checking all books

Book.objects.all()

# Expected Output: <QuerySet []>
