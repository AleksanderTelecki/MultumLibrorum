from django.urls import include, path
from . import views


urlpatterns = [
    path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/register/', views.registerUser, name='register'),
    path('users/profile/', views.getUserProfile, name="users-profile"),
    path('users/', views.getUsers, name="users"),
    path('books/', views.APIBookListView.as_view(), name="books"),
    path('books/<str:pk>/', views.getBook, name="book")
]
