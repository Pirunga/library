from django.contrib import admin
from bookcase.models import Book, Author

admin.site.register(Book)
admin.site.register(Author)