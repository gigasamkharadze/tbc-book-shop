from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core.serializers import serialize
from django.core.paginator import Paginator

from market.models import Book


# Create your views here.
def home(request):
    return render(request, 'main.html')


def all_books(request):
    books = Book.objects.all()
    paginator = Paginator(books, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'books.html', {'page_obj': page_obj})


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})
