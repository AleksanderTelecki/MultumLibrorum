from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

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


class APIBookListView(ListAPIView):
    queryset = Book.objects.get_queryset().order_by('_id')
    serializer_class = BookSerializer
    pagination_class = PageNumberPagination


@api_view(['GET'])
def getBook(request, pk):
    book = Book.objects.get(_id=pk)
    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)
