from rest_framework.viewsets import ModelViewSet

from book_store.api.serializers import BookSerializer
from book_store.models import Book


class BookViewSet(ModelViewSet):
    permission_classes = ()
    authentication_classes = ()
    serializer_class = BookSerializer
    queryset = Book.objects.all()
