import random

from django.core.management.base import BaseCommand

from book_store.factory import AuthorFactory, PublishingHouseFactory, TagsFactory, BookFactory


class Command(BaseCommand):
    """
    This command is for inserting Publisher, Book, Store into database.
    Insert 5 Publishers, 100 Books, 10 Stores.
    """

    def handle(self, *args, **options):
        # create 5 publishers
        publishers = PublishingHouseFactory.create_batch(5)

        # create 10 authors
        authors = AuthorFactory.create_batch(10)

        # create 10 tags
        tags = TagsFactory.create_batch(10)

        # create 25 books for every author (5 each belonging to a publishing house) and assign random tags
        for author in authors:
            for publisher in publishers:
                book_tags = random.sample(tags, random.randrange(10))
                books = BookFactory.create_batch(5, author=author, publishing_house=publisher, tags=book_tags)
