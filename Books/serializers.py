from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['UserID', 'Name', 'Email', 'MembershipDate']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['BookID', 'Title', 'ISBN', 'PublishedDate', 'Genre']

class BookDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookDetails
        fields = ['NumberOfPages', 'Publisher', 'Language']

class BorrowedBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowedBooks
        fields = ['user', 'book', 'BorrowDate', 'ReturnDate']