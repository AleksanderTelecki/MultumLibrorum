from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def getRoutes(request):
    routes = ['/api/books/',
              '/api/books/create',
              '/api/books/upload']
    return JsonResponse(routes, safe=False)
