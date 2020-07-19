from django.http import HttpResponse

def index(request):
    return HttpResponse("hello World")

def home(request):
    return HttpResponse("<h1>welcome to Home Page<h1>")