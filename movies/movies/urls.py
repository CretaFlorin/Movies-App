from django.contrib import admin
from django.urls import path

from viewer.views import home_page, HomePage, HomePageListView, MovieCreateView, MovieUpdateView, MovieDeleteView
from viewer.models import Genre, Movie

admin.site.register(Genre)
admin.site.register(Movie)

urlpatterns = [
    path("admin/", admin.site.urls),

    # Home
    path("", HomePageListView.as_view(), name="home"),
    
    # CRUD
    path("movies/create/", MovieCreateView.as_view(), name="movie_create"),
    path("movies/update/<pk>", MovieUpdateView.as_view(), name="movie_update"),
    path("movies/delete/<pk>", MovieDeleteView.as_view(), name="movie_delete"),
]
