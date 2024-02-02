from rest_framework import serializers
from .models import User, Book, BookDetails, BorrowedBooks


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model.
    """
    class Meta:
        model = User
        fields = ['UserID', 'Name', 'Email', 'MembershipDate']


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for Book model.
    """
    class Meta:
        model = Book
        fields = ['BookID', 'Title', 'ISBN', 'PublishedDate', 'Genre']


class BookDetailsSerializer(serializers.ModelSerializer):
    """
    Serializer for BookDetails model.
    """
    class Meta:
        model = BookDetails
        fields = ['NumberOfPages', 'Publisher', 'Language']


class BorrowedBooksSerializer(serializers.ModelSerializer):
    """
    Serializer for BorrowedBooks model.
    """
    class Meta:
        model = BorrowedBooks
        fields = ['user', 'book', 'BorrowDate', 'ReturnDate']

    def validate(self, data):
        """
        Custom validation to ensure BorrowDate is before ReturnDate.
        """
        borrow_date = data.get('BorrowDate')
        return_date = data.get('ReturnDate')

        if borrow_date and return_date and borrow_date > return_date:
            raise serializers.ValidationError("ReturnDate must be after BorrowDate.")

        return data
