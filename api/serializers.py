from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book, Language


class BookSerializer(serializers.ModelSerializer):
    language = serializers.SlugRelatedField(
        many=True,
        queryset=Language.objects.all(),
        slug_field='name'
     )

    author = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )





    class Meta:
        model = Book
        fields = '__all__'
        # depth = 1
