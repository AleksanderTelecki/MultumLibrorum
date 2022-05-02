from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book, Language, Genres, Author, BookShelf


# TODO: ADD MORE SERIALIZERS
class BookSerializer(serializers.ModelSerializer):
    language = serializers.SlugRelatedField(
        many=True,
        queryset=Language.objects.all(),
        slug_field='name'
    )

    author = serializers.SlugRelatedField(
        many=True,
        queryset=Author.objects.all(),
        slug_field='name'
    )

    genres = serializers.SlugRelatedField(
        many=True,
        queryset=Genres.objects.all(),
        slug_field='name'
    )

    bookshelf = serializers.SlugRelatedField(
        many=True,
        queryset=BookShelf.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Book
        fields = '__all__'
        # depth = 1
