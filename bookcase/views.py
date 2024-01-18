from rest_framework.viewsets import ModelViewSet
from bookcase.models import Book, Author
from bookcase.serializers import BookSerializer, AuthorSerializer

class BooksViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class AuthorsViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
