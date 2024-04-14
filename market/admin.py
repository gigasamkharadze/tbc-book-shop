from django.contrib import admin
from market.models import Book, Author, Category


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'page_count', 'category', 'cover', 'author', 'price', 'image']
    search_fields = ['name', 'author__first_name']

    def author(self, obj):
        return f'{obj.author.first_name} {obj.author.last_name}'


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_birth', 'country']
    search_fields = ['first_name', 'last_name']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
