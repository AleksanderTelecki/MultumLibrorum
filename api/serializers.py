from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Book, Language, Genres, Author, BookShelf, Publisher
from djoser.serializers import UserCreateSerializer

User = get_user_model()


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

    publisher = serializers.SlugRelatedField(
        many=False,
        queryset=Publisher.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Book
        fields = '__all__'
        # depth = 1


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = '__all__'


class UserSerializer(UserCreateSerializer):
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)
    name = serializers.SerializerMethodField(read_only=True)

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['_id', 'email', 'name', 'username', 'password', 'isAdmin']

    def get_isAdmin(self, obj):
        return obj.is_staff

    def get__id(self, obj):
        return obj.id

    def get_name(self, obj):
        name = obj.first_name + obj.last_name
        return name

