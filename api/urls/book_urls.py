from django.urls import include, path
from api.views import book_views

urlpatterns = [
    path('', book_views.APIBookListView.as_view(), name="books"),
    path('<str:pk>/', book_views.getBook, name="book")
]