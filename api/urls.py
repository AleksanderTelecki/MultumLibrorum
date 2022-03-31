from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('books/', views.getBooks, name="books"),
    path('books/<str:pk>/', views.getBook, name="book")
]
