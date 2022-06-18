from django.contrib.auth import get_user_model
from django.db.models import Prefetch
from rest_framework.serializers import ModelSerializer

from book_store.models import Book, Author, PublishingHouse, Tags

User = get_user_model()


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email", "username")


class AuthorSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Author
        fields = "__all__"


class PublishingHouseSerializer(ModelSerializer):
    class Meta:
        model = PublishingHouse
        fields = "__all__"


class TagsSerializer(ModelSerializer):
    class Meta:
        model = Tags
        fields = "__all__"


class BookSerializer(ModelSerializer):
    author = AuthorSerializer()
    publishing_house = PublishingHouseSerializer()
    tags = TagsSerializer(many=True)

    class Meta:
        model = Book
        fields = "__all__"

    @classmethod
    def setup_eager_loading(cls, queryset):
        author_prefetch = Prefetch("author", queryset=Author.objects.select_related("user"))
        queryset = queryset.select_related("publishing_house").prefetch_related("tags", author_prefetch)
        return queryset
