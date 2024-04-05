from django.urls import path
from .views import all_books, book_detail, home


urlpatterns = [
    path('', home),
    path('books/', all_books),
    path('books/<int:book_id>/', book_detail),
]
