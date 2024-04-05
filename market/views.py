from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize
from .models import Book


# Create your views here.
def home(request):
    return render(request, 'main.html')


def all_books(request):
    books = Book.objects.all()
    serialized_books = serialize('json', books)
    return JsonResponse(serialized_books, safe=False)


def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    serialized_book = serialize('json', [book])
    return JsonResponse(serialized_book, safe=False)
