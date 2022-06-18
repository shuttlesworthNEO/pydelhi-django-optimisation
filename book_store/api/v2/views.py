from rest_framework.viewsets import ModelViewSet

from book_store.api.v2.serializers import BookSerializer
from book_store.models import Book


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get_queryset(self):
        queryset = Book.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset
