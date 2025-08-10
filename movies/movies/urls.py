from django.contrib import admin
from django.urls import path

from viewer.views import home_page, HomePage, HomePageListView
from viewer.models import Genre, Movie

admin.site.register(Genre)
admin.site.register(Movie)

urlpatterns = [
    path("admin/", admin.site.urls),
    #
    # path("", home_page),
    # path("", HomePage.as_view()),
    path("", HomePageListView.as_view()),
]
