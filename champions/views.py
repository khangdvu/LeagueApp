from django.http import HttpResponse
from django.template import loader
from .models import Champion
from rest_framework import viewsets
from .serializers import ChampionSerializer

""" def index(request):
    all_champions = Champion.objects.all()
    template = loader.get_template('champions/champions.html')
    context = {
        'all_champions' : all_champions,
    }
    return HttpResponse(template.render(context, request))
 """

class ChampionViewSet(viewsets.ModelViewSet):
    queryset = Champion.objects.all().order_by('hp')
    serializer_class = ChampionSerializer
