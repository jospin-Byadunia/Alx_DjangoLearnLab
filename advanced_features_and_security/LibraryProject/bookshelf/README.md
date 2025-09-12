# Permissions and Groups Setup

This app uses Django’s built-in permissions system with custom rules for the `Book` model.

## Custom Permissions

- `can_view` → View books
- `can_create` → Create new books
- `can_edit` → Edit existing books
- `can_delete` → Delete books

## Groups

- **Editors** → Assigned `can_create`, `can_edit`
- **Viewers** → Assigned `can_view`
- **Admins** → Assigned all permissions

## Enforcement

Views use the `@permission_required` decorator to enforce rules. Example:

```python
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404, render, redirect
from .models import Book
from .forms import BookForm

@permission_required("bookshelf.can_edit", raise_exception=True)
def edit_book_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("view_book")
    else:
        form = BookForm(instance=book)
    return render(request, "bookshelf/edit_book.html", {"form": form})
```
