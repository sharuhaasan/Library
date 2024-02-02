from django.urls import path
from . import views

urlpatterns = [
    # Users
    path('users/', views.CreateUserView.as_view(), name='create-user'),
    path('users/all/', views.ListAllUsersView.as_view(), name='list-all-users'),
    path('users/<int:UserID>/', views.GetUserByIDView.as_view(), name='get-user-by-id'),

    # Books
    path('books/', views.AddNewBookView.as_view(), name='add-new-book'),
    path('books/all/', views.ListAllBooksView.as_view(), name='list-all-books'),
    path('books/<int:BookID>/', views.GetBookByIDView.as_view(), name='get-book-by-id'),

    # Book Details
    path('books/details/<int:Book_id>/', views.AssignOrUpdateBookDetailsView.as_view(), name='assign-update-book-details'),

    # Borrowing Books
    path('borrow/', views.BorrowBookView.as_view(), name='borrow-book'),
    path('return/<int:pk>/', views.ReturnBookView.as_view(), name='return-book'),
    path('borrowed-books/', views.ListAllBorrowedBooksView.as_view(), name='list-all-borrowed-books'),
]
