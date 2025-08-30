from library.models import Book

# Retrieve the book you created

book = Book.objects.get(title="1984")

# Expected Output: Book object with all attributes

book.title # "1984"
book.author # "George Orwell"
book.published # 1949
