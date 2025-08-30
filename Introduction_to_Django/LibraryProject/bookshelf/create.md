from library.models import Book

# Create a Book instance

book = Book.objects.create(title="1984", author="George Orwell", published=1949)

# Expected Output: A Book instance created successfully

book

# <Book: Book object (1)>
