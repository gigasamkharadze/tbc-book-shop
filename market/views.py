from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from market.models import Book


# Create your views here.
def home(request):
    return render(request, 'main.html')


def all_books(request):
    books = Book.objects.all()

    author = request.GET.get('author')
    category = request.GET.get('category')

    if category:
        books = books.filter(categories__name=category)

    if author:
        books = books.filter(author__first_name__startswith=author)

    paginator = Paginator(books, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'books.html', {'page_obj': page_obj})


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})
