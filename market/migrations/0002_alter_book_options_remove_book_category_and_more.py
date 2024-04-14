# Generated by Django 5.0.4 on 2024-04-14 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['name', 'price', 'page_count', 'author'], 'verbose_name': 'book', 'verbose_name_plural': 'books'},
        ),
        migrations.RemoveField(
            model_name='book',
            name='category',
        ),
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(related_name='books', to='market.category', verbose_name='category'),
        ),
    ]
