from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('name'))
    page_count = models.IntegerField(verbose_name=_('page count'))
    category = models.CharField(max_length=100, verbose_name=_('category'))
    author_name = models.CharField(max_length=100, verbose_name=_('author name'))
    price = models.IntegerField(verbose_name='Price')
    image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name=_('image'))

    def __str__(self):
        return f'{self.name} written by {self.author_name}'

    class Meta:
        verbose_name = _('book')
        verbose_name_plural = _('books')
        ordering = ['name', 'price', 'page_count', 'author_name']
        indexes = [
            models.Index(fields=['name'], name='name_idx'),
            models.Index(fields=['price'], name='price_idx'),
            models.Index(fields=['page_count'], name='page_count_idx'),
            models.Index(fields=['author_name'], name='author_name_idx')
        ]
        constraints = [
            models.UniqueConstraint(fields=['name', 'author_name'], name='unique_book')
        ]
