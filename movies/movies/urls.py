from django.contrib import admin
from django.urls import path

from viewer.views import (
    HomePageListView,
    MovieCreateView,
    MovieUpdateView,
    MovieDeleteView,
    CustomLoginView,
    CustomRegisterView,
    logout_view,
)
from viewer.models import Genre, Movie

admin.site.register(Genre)
admin.site.register(Movie)

urlpatterns = [
    path("admin/", admin.site.urls),
    # Auth
    path("accounts/login/", CustomLoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path('signup/', CustomRegisterView.as_view(), name='register'),
    # Home
    path("", HomePageListView.as_view(), name="home"),
    # CRUD
    path("movies/create/", MovieCreateView.as_view(), name="movie_create"),
    path("movies/update/<pk>", MovieUpdateView.as_view(), name="movie_update"),
    path("movies/delete/<pk>", MovieDeleteView.as_view(), name="movie_delete"),
]
