from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> Champions page placeholder</h1>")
