from django.contrib import admin
from market.models import Book, Author, Category


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'page_count', 'categories_display', 'cover', 'author_display', 'price', 'image']
    search_fields = ['name', 'author__first_name']

    def categories_display(self, obj):
        return ', '.join([category.name for category in obj.categories.all()])
    categories_display.short_description = 'Categories'

    @staticmethod
    def author_display(obj):
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
