from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from viewer.models import Movie, Genre

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