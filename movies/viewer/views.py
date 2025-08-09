from django.shortcuts import render
from django.http import HttpResponse

# http://127.0.0.1:8000/hello/Florin
def hello_view1(request, name):
    return HttpResponse(f"Hello {name}!!")

# http://127.0.0.1:8000/hello/?name=Florin
def hello_view2(request):
    name = request.GET.get('name')
    return HttpResponse(f"Hello {name}!!")