from django.db import models

# Model for Author


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Model for Book with ForeignKey to Author

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        Author, related_name='books', on_delete=models.CASCADE)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title
