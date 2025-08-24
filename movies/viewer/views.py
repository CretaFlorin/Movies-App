from django.shortcuts import render
from django.views.generic import TemplateView, ListView, FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

from viewer.models import Movie, Genre
from viewer.forms.movie_form import MovieForm



# Functional View
def home_page(request):
    movies = Movie.objects.all()
    return render(
        request, 
        template_name="home_page.html", 
        context={"movies": movies}
    )

# CBV (Class-Based Views)
class HomePage(TemplateView):
    template_name = "home_page.html"
    movies = Movie.objects.all()
    extra_context = {"movies": movies}


class HomePageListView(ListView):
    template_name = "home_page.html"
    model = Movie

# CRUD for Movie
class MovieCreateView(CreateView):
    template_name = 'form.html'
    form_class = MovieForm
    success_url = reverse_lazy("home")


class MovieUpdateView(UpdateView):
    template_name = 'form.html'
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy("home")


class MovieDeleteView(DeleteView):
    template_name = 'movie_delete_confirm.html'
    model = Movie
    success_url = reverse_lazy("home")

# Auth
class CustomLoginView(LoginView):
    template_name = "form.html"

def logout_view(request):
    logout(request)
    return redirect('login')

class CustomRegisterView(CreateView):
    template_name = 'form.html'
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
