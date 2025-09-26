from django.contrib.auth.models import User, Permission
from rest_framework import test
from rest_framework import status
from .models import Book


class BookAPITestCase(test.APITestCase):
    def setUp(self):
        # Create user with and without permissions
        self.user = User.objects.create_user(username="user", password="pass123")
        self.admin = User.objects.create_user(username="admin", password="pass123")
        self.admin.user_permissions.add(Permission.objects.get(codename="add_book"))
        self.admin.user_permissions.add(Permission.objects.get(codename="change_book"))
        self.admin.user_permissions.add(Permission.objects.get(codename="delete_book"))

        # Test book
        self.book = Book.objects.create(
            title="Test Book", author="Tester", publication_year=2021
        )

    def test_list_books(self):
        """Anyone should be able to list books"""
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_book_unauthorized(self):
        """Unauthorized user cannot create books"""
        response = self.client.post("/api/books/", {
            "title": "New Book",
            "author": "Author X",
            "publication_year": 2022
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_book_authorized(self):
        """User with permission can create books"""
        self.client.login(username="admin", password="pass123")
        response = self.client.post("/api/books/", {
            "title": "New Book",
            "author": "Author X",
            "publication_year": 2022
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):
        """Authorized user can update a book"""
        self.client.login(username="admin", password="pass123")
        response = self.client.patch(f"/api/books/{self.book.id}/", {
            "title": "Updated Title"
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Title")

    def test_delete_book(self):
        """Authorized user can delete a book"""
        self.client.login(username="admin", password="pass123")
        response = self.client.delete(f"/api/books/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    def test_permission_enforcement(self):
        """Ensure normal user cannot update or delete"""
        self.client.login(username="user", password="pass123")
        response = self.client.patch(f"/api/books/{self.book.id}/", {"title": "Hack"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
