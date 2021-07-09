from django.http import HttpResponse
from django.template import loader
from .models import Champion
from rest_framework import viewsets
from .serializers import ChampionSerializer


class ChampionViewSet(viewsets.ModelViewSet):
    queryset = Champion.objects.all().order_by('name')
    serializer_class = ChampionSerializer
