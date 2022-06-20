from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from ..models import Book, Genres
from ..serializers import BookSerializer, GenreSerializer


class APIBookListView(ListCreateAPIView):
    queryset = Book.objects.get_queryset().order_by('_id')
    serializer_class = BookSerializer
    pagination_class = PageNumberPagination

    parser_classes = [JSONParser]

    # TODO: REFACTOR
    def post(self, request, format=None):
        print(request.data)
        if 'genres' in request.data:
            books = Book.objects.filter(genres___id__in=request.data['genres'])
            serialized_books = BookSerializer(books, many=True)
        if 'search' in request.data:
            books = Book.objects.filter(title__icontains=request.data['search'])
            serialized_books = BookSerializer(books, many=True)
        return Response(serialized_books.data)


class APIGenresView(ListAPIView):
    queryset = Genres.objects.get_queryset().order_by('_id')
    serializer_class = GenreSerializer
    pagination_class = PageNumberPagination


@api_view(['GET'])
def getBook(request, pk):
    book = Book.objects.get(_id=pk)
    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)
