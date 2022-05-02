from django.shortcuts import render
from django.http import JsonResponse
from .books import books
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from .utils import gutenbergDataMigrator


@api_view(['GET'])
def getRoutes(request):
    routes = ['/api/books/',
              '/api/books/create',
              '/api/books/upload']
    return Response(routes)


@api_view(['GET'])
def getBooks(request):
    books = Book.objects.all()
    serializedBooks = BookSerializer(books, many=True)
    return Response(serializedBooks.data)


@api_view(['GET'])
def getBook(request, pk):
    book = Book.objects.get(_id=pk)
    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)
