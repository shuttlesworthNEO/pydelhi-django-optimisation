import factory
from django.contrib.auth import get_user_model
from factory.django import DjangoModelFactory

from book_store.models import Author, PublishingHouse, Tags, Book

User = get_user_model()


class UserFactory(DjangoModelFactory):
    email = factory.Sequence(lambda n: f"user{n}@domain.com")
    first_name = factory.Faker("word")
    last_name = factory.Faker("word")
    username = factory.Sequence(lambda n: f"username{n}")

    class Meta:
        model = User
        django_get_or_create = ("username",)


class AuthorFactory(DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    pseudonym = factory.Sequence(lambda n: f"Author Pseudonym {n}")

    class Meta:
        model = Author
        django_get_or_create = ("user",)


class PublishingHouseFactory(DjangoModelFactory):
    name = factory.Faker("word")
    about = factory.Faker("text")
    address = factory.Faker("text")

    class Meta:
        model = PublishingHouse


class TagsFactory(DjangoModelFactory):
    title = factory.Faker("word")
    description = factory.Faker("text")

    class Meta:
        model = Tags


class BookFactory(DjangoModelFactory):
    title = factory.Faker("word")
    description = factory.Faker("text")
    author = factory.SubFactory(AuthorFactory)
    publishing_house = factory.SubFactory(PublishingHouseFactory)

    class Meta:
        model = Book

    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if extracted and create:
            if not isinstance(extracted, (list, set, tuple)):
                extracted = (extracted,)
            self.tags.add(*extracted)
