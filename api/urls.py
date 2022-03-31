from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.getRoutes, name="routes")
]
