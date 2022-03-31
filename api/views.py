from django.shortcuts import render
from django.http import JsonResponse
from .books import books
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def getRoutes(request):
    routes = ['/api/books/',
              '/api/books/create',
              '/api/books/upload']
    return Response(routes)


@api_view(['GET'])
def getBooks(request):
    return Response(books)


@api_view(['GET'])
def getBook(request, pk):
    book = None
    for item in books:
        if item['_id'] == pk:
            book = item
            break

    return Response(book)
