from rest_framework import serializers
from bookApp.models import Author, Book, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ["book", "id"]


class BookSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):

    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = "__all__"
