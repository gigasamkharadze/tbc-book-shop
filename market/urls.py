from django.urls import path
from .views import all_books, book_detail, home

app_name = 'market'

urlpatterns = [
    path('', home),
    path('books/', all_books, name='all_books'),
    path('books/<int:book_id>/', book_detail, name='book_detail'),
]
