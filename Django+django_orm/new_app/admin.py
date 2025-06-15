from django.contrib import admin

from .models import Author, Book, Review


@admin.register(Author)
class AdminAuthor(admin.ModelAdmin):
    fields = ['id']
    list_display = ['id']


@admin.register(Book)
class AdminAuthor(admin.ModelAdmin):
    fields = ['id']
    list_display = ['id']


@admin.register(Review)
class AdminAuthor(admin.ModelAdmin):
    fields = ['id']
    list_display = ['id']
