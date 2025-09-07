from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Book(models.Model):
    title= models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    class Meta:
        permissions = [
            ("can_add_book", "Can add a new book"),
            ("can_change_book", "Can change existing book"),
            ("can_delete_book", "Can delete a book"),
        ]

class Library(models.Model):
    name= models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='libraries')
    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length = 100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    role = models.CharField(choices=[('admin', 'Admin'),('member', 'Member'), ('librarian', 'Librarian')], max_length=20)
    def __str__(self):
        return f"{self.user.username}'s profile"