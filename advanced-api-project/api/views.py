from django.shortcuts import render
from rest_framework import generics
from .models import Book, Author    
from .serializers import BookSerializer, AuthorSerializer, serializers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

# list all books

class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes =[IsAuthenticatedOrReadOnly]

# detail view of a book
class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes =[IsAuthenticatedOrReadOnly]
    
# Adding a new book
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Allow any user (authenticated or not) to access this view
    
    def perform_create(self, serializer):
        title = serializer.validated_data.get("title")
        if Book.objects.filter(title=title).exists():
            raise serializers.ValidationError({"title": "A book with this title already exists."})
        
        # Save with additional field (if your Book model has a 'created_by' field for example)
        serializer.save(created_by=self.request.user)

# Updating a book
class UpdateView (generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        # Example: Only allow the original creator to edit the book
        book = self.get_object()
        if book.created_by != self.request.user:
            raise permissions.PermissionDenied("You do not have permission to edit this book.")

        serializer.save()
    
# Deleting a book
class DeleteView (generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # ✅ Only admins can delete
