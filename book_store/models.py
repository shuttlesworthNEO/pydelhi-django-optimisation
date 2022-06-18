from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pseudonym = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PublishingHouse(models.Model):
    name = models.CharField(max_length=256)
    about = models.TextField()
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tags(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Book(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    publishing_house = models.ForeignKey(PublishingHouse, on_delete=models.CASCADE, related_name="books")
    tags = models.ManyToManyField(Tags)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    delete = models.DateTimeField(null=True)
