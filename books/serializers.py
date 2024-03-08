from rest_framework import serializers
from .models import Book, Request


class BookSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = Book
        fields = ["name", "image", "author", "owner", "duration", "lent"]


class RequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Request
        fields = "__all__"
