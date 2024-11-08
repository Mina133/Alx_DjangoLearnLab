from django.contrib import admin
from .models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author', 'publication_year')
    ordering = ['title']

admin.site.register(Book, BookAdmin)