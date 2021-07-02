from rest_framework import serializers

from .models import Champion

class ChampionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Champion
        fields = '__all__'