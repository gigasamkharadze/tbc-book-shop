# Generated by Django 5.0.4 on 2024-04-14 11:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('page_count', models.IntegerField(verbose_name='page count')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('cover', models.CharField(choices=[('HC', 'Hard cover'), ('SC', 'Soft cover'), ('SPC', 'Special cover')], default='SC', max_length=3, verbose_name='cover type')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='image')),
            ],
            options={
                'verbose_name': 'book',
                'verbose_name_plural': 'books',
                'ordering': ['name', 'price', 'page_count', 'category', 'author'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='first name')),
                ('last_name', models.CharField(max_length=100, verbose_name='last name')),
                ('date_of_birth', models.DateField(null=True, verbose_name='date of birth')),
                ('country', models.CharField(max_length=100, verbose_name='country')),
            ],
            options={
                'verbose_name': 'author',
                'verbose_name_plural': 'authors',
                'ordering': ['first_name', 'last_name', 'date_of_birth'],
                'indexes': [models.Index(fields=['first_name'], name='first_name_idx'), models.Index(fields=['last_name'], name='last_name_idx')],
            },
        ),
        migrations.AddConstraint(
            model_name='author',
            constraint=models.UniqueConstraint(fields=('first_name', 'last_name'), name='unique_author'),
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='market.author', verbose_name='author'),
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['name'], name='name_idx'),
        ),
        migrations.AddConstraint(
            model_name='category',
            constraint=models.UniqueConstraint(fields=('name',), name='unique_category'),
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='market.category', verbose_name='category'),
        ),
        migrations.AddIndex(
            model_name='book',
            index=models.Index(fields=['price'], name='price_idx'),
        ),
        migrations.AddIndex(
            model_name='book',
            index=models.Index(fields=['page_count'], name='page_count_idx'),
        ),
    ]
