from django.urls import include, path
from . import views


urlpatterns = [
    path('users/login', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/profile/', views.getUserProfile, name="users-profile"),
    path('users/', views.getUsers, name="users"),
    path('', views.getRoutes, name="routes"),
    path('books/', views.APIBookListView.as_view(), name="books"),
    path('books/<str:pk>/', views.getBook, name="book")
]
