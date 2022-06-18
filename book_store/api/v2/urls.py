from django.conf.urls import include
from django.urls import path
from rest_framework.routers import SimpleRouter

from book_store.api.v2.views import BookViewSet

router = SimpleRouter()


router.register(r"books", BookViewSet, "book-store-books")
urlpatterns = [
    path("", include(router.urls)),
]
