from django.contrib import admin
from django.urls import path

from viewer.views import hello_view1, hello_view2

urlpatterns = [
    # Regex
    path('hello/<name>', hello_view1),

    # Query params
    path('hello/', hello_view2),
]