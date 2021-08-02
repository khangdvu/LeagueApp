from django.http import HttpResponse, response
from django.template import loader
from .models import Champion
from rest_framework import viewsets
from .serializers import ChampionSerializer
import json


class ChampionViewSet(viewsets.ModelViewSet):
    queryset = Champion.objects.all().order_by('name')
    serializer_class = ChampionSerializer

def getChampion(request, champName, itemSet):
    responseData = {}
    champion = Champion.objects.get(name = champName)
    responseData['name'] = champion.name
    responseData['sprite'] = champion.sprite
    return HttpResponse(json.dumps(responseData), content_type="application/json")