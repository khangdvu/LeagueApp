from django.http import HttpResponse
from django.template import loader
from .models import Champion

def index(request):
    all_champions = Champion.objects.all()
    template = loader.get_template('champions/champions.html')
    context = {
        'all_champions' : all_champions,
    }
    return HttpResponse(template.render(context, request))
