from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.core.serializers import serialize

from market.models import Book


# Create your views here.
def home(request):
    return render(request, 'main.html')


def all_books(request):
    books = Book.objects.all()
    serialized_books = serialize('json', books)
    return JsonResponse(serialized_books, safe=False)


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    serialized_book = serialize('json', [book])
    return JsonResponse(serialized_book, safe=False)
