from django.db import models
from django.utils.translation import gettext as _
from .choices import COVER_CHOICES


# Create your models here.
class Book(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='books', verbose_name=_('author'))
    categories = models.ManyToManyField('Category', related_name='books', verbose_name=_('categories'))
    name = models.CharField(max_length=100, verbose_name=_('name'))
    page_count = models.IntegerField(verbose_name=_('page count'))
    price = models.IntegerField(verbose_name='Price')
    cover = models.CharField(max_length=3, choices=COVER_CHOICES, default=None, verbose_name=_('cover type'))
    image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name=_('image'))

    def __str__(self):
        return f'{self.name} written by {self.author.first_name}'

    class Meta:
        verbose_name = _('book')
        verbose_name_plural = _('books')
        ordering = ['name', 'price', 'page_count', 'author']
        indexes = [
            models.Index(fields=['price'], name='price_idx'),
            models.Index(fields=['page_count'], name='page_count_idx'),
        ]


class Author(models.Model):
    first_name = models.CharField(max_length=100, verbose_name=_('first name'))
    last_name = models.CharField(max_length=100, verbose_name=_('last name'))
    date_of_birth = models.DateField(null=True, verbose_name=_('date of birth'))
    country = models.CharField(max_length=100, verbose_name=_('country'))

    def __str__(self):
        return f'{self.first_name} {self.last_name} from {self.country}. birth date: {self.date_of_birth}'

    class Meta:
        verbose_name = _('author')
        verbose_name_plural = _('authors')
        ordering = ['first_name', 'last_name', 'date_of_birth']
        indexes = [
            models.Index(fields=['first_name'], name='first_name_idx'),
            models.Index(fields=['last_name'], name='last_name_idx'),
        ]
        constraints = [
            models.UniqueConstraint(fields=['first_name', 'last_name'], name='unique_author'),
        ]


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('name'))

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'], name='name_idx'),
        ]
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_category'),
        ]
