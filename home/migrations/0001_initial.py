# Generated by Django 3.2.9 on 2022-08-13 16:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('image', models.ImageField(blank=True, upload_to='image/%Y/%m', verbose_name='Image')),
                ('slug', models.SlugField(max_length=225, null=True, unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('slug', models.SlugField(max_length=225, null=True, unique=True, verbose_name='Slug')),
                ('order', models.IntegerField(blank=True, null=True, unique=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='home.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name_plural': 'Subcategories',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('description', models.TextField(blank=True, max_length=500, verbose_name='Description')),
                ('content', models.TextField(blank=True, verbose_name='Content')),
                ('html_content', models.TextField(blank=True, verbose_name='HTML Content')),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='Data')),
                ('update_data', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('is_published', models.BooleanField(default=True, verbose_name='Publish')),
                ('image', models.ImageField(blank=True, upload_to='image/%Y/%m', verbose_name='Image')),
                ('slug', models.SlugField(max_length=225, null=True, unique=True, verbose_name='URL-name')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.category', verbose_name='Category')),
                ('subcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.subcategory', verbose_name='Subcategory')),
            ],
            options={
                'verbose_name_plural': 'Topics',
                'ordering': ['id'],
            },
        ),
    ]
