from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from book_store.models import Book, Author, PublishingHouse, Tags

User = get_user_model()


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


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
