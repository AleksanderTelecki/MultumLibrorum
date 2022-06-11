from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Book, Language, Genres, Author, BookShelf,Publisher


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

    publisher = serializers.SlugRelatedField(
        many=False,
        queryset=Publisher.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Book
        fields = '__all__'
        # depth = 1


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin']

    def get_isAdmin(self, obj):
        return obj.is_staff

    def get__id(self, obj):
        return obj.id

    def get_name(self, obj):
        name = obj.first_name
        return name


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)
