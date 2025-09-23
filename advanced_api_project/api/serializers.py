from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

# Serializer for Book model


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

# Serializer for Author model with nested BookSerializer


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = 'name'

    def validate(self, data):
        if data['publication_year'] > datetime.now().year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future.")
