from bookshelf.models import Book

# Get the book

book = Book.objects.get(title="1984")

# Update the title

book.title = "Nineteen Eighty-Four"
book.save()

# Expected Output: Updated title

book.title

# "Nineteen Eighty-Four"
