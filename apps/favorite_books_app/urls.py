from django.urls import path
from . import views

urlpatterns = [
    path('books', views.books), #GET request to display all books'
    path('books/create', views.create_book), #POST request to create an book
    path('books/<int:book_id>', views.view_book), #GET request to display a specific book's info
    path('books/<int:book_id>/update', views.update_book), #POST request to update a specific book
    path('books/<int:book_id>/favorite', views.favorite_book), #POST request to update a specific book
    path('books/<int:book_id>/unfavorite', views.unfavorite_book), #POST request to update a specific book
    path('books/<int:book_id>/delete', views.delete_book), #POST request to delete a specific book
]