from django.test import TestCase
from django.urls import reverse
from datetime import datetime
from rest_framework import status
from rest_framework.test import APIClient
from .models import *

class CreateUserViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_user(self):
        url = reverse('create-user')
        data = {
            'UserID': '1',
            'Name': 'testname',
            'Email': 'test@example.com',
            'MembershipDate': '2024-02-02'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().Name, 'testname')

class ListAllUsersViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(UserID='1', Name='testname', Email='test@example.com', MembershipDate='2024-02-02')

    def test_list_all_users(self):
        url = reverse('list-all-users')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

class GetUserByIDViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(UserID='1',Name='testname', Email='test@example.com', MembershipDate='2024-02-02')

    def test_get_user_by_id(self):
        url = reverse('get-user-by-id', args=[self.user.UserID])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['Name'], 'testname')
class BookAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_book(self):
        url = reverse('add-new-book')
        data = {
            'BookID': '1',
            'Title': 'Test Book',
            'ISBN': '1234567890',
            'PublishedDate': '2024-01-01',
            'Genre': 'Test Genre'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().Title, 'Test Book')

class ListAllBooksViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.book = Book.objects.create(BookID='1', Title='Test Book', ISBN='1234567890', PublishedDate='2024-01-01', Genre='Test Genre')

    def test_list_all_books(self):
        url = reverse('list-all-books')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

class GetBookByIDViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.book = Book.objects.create(BookID='1', Title='Test Book', ISBN='1234567890', PublishedDate='2024-01-01', Genre='Test Genre')

    def test_get_book_by_id(self):
        url = reverse('get-book-by-id', args=[self.book.BookID])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['Title'], 'Test Book')


class BorrowBookViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(UserID='1',Name='testname', Email='test@example.com', MembershipDate='2024-02-02')
        self.book = Book.objects.create(BookID='1', Title='Test Book', ISBN='1234567890', PublishedDate='2024-01-01', Genre='Test Genre')

    def test_borrow_book(self):
        url = reverse('borrow-book')
        data = {
            'user': self.user.UserID,
            'book': self.book.BookID,
            'BorrowDate': '2024-02-01'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BorrowedBooks.objects.count(), 1)

class ReturnBookViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(UserID='1', Name='testname', Email='test@example.com', MembershipDate='2024-02-02')
        self.book = Book.objects.create(BookID='1', Title='Test Book', ISBN='1234567890', PublishedDate='2024-01-01', Genre='Test Genre')
        self.borrowed_book = BorrowedBooks.objects.create(user=self.user, book=self.book, BorrowDate=datetime.now())

    def test_return_book(self):
        url = reverse('return-book', args=[self.borrowed_book.id])
        data = {'ReturnDate': '2024-02-15'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(BorrowedBooks.objects.get(id=self.borrowed_book.id).ReturnDate, datetime.strptime('2024-02-15', '%Y-%m-%d').date())


class ListAllBorrowedBooksViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(UserID='1', Name='testname', Email='test@example.com', MembershipDate='2024-02-02')
        self.book = Book.objects.create(BookID='1', Title='Test Book', ISBN='1234567890', PublishedDate='2024-01-01', Genre='Test Genre')
        self.borrowed_book = BorrowedBooks.objects.create(user=self.user, book=self.book, BorrowDate=datetime.now())

    def test_list_all_borrowed_books(self):
        url = reverse('list-all-borrowed-books')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)