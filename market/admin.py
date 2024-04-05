from django.contrib import admin
from .models import Book


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'page_count', 'category', 'author_name', 'price', 'image']
    search_fields = ['name', 'author_name']


admin.site.register(Book, BookAdmin)
