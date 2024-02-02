from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import *
from .models import *


class CreateUserView(generics.CreateAPIView):
    """
    API endpoint to create a new user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListAllUsersView(generics.ListAPIView):
    """
    API endpoint to list all users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GetUserByIDView(generics.RetrieveAPIView):
    """
    API endpoint to retrieve a user by ID.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'UserID'


class AddNewBookView(generics.CreateAPIView):
    """
    API endpoint to add a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ListAllBooksView(generics.ListAPIView):
    """
    API endpoint to list all books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class GetBookByIDView(generics.RetrieveAPIView):
    """
    API endpoint to retrieve a book by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'BookID'


class AssignOrUpdateBookDetailsView(generics.UpdateAPIView):
    """
    API endpoint to assign or update book details.
    """
    queryset = BookDetails.objects.all()
    serializer_class = BookDetailsSerializer
    lookup_field = 'Book_id'


class BorrowBookView(generics.CreateAPIView):
    """
    API endpoint to borrow a book.
    """
    queryset = BorrowedBooks.objects.all()
    serializer_class = BorrowedBooksSerializer


class ReturnBookView(generics.UpdateAPIView):
    """
    API endpoint to return a borrowed book.
    """
    queryset = BorrowedBooks.objects.all()
    serializer_class = BorrowedBooksSerializer

    def update(self, request, *args, **kwargs):
        """
        Update the return date of a borrowed book.
        """
        instance = self.get_object()
        instance.ReturnDate = request.data.get('ReturnDate')
        instance.save()
        return Response(self.get_serializer(instance).data)


class ListAllBorrowedBooksView(generics.ListAPIView):
    """
    API endpoint to list all borrowed books.
    """
    queryset = BorrowedBooks.objects.all()
    serializer_class = BorrowedBooksSerializer
