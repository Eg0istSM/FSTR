from rest_framework import serializers
from .models import *


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ('latitude', 'longitude', 'height',)


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('winter', 'summer', 'autumn', 'spring',)


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('data', 'title',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'fam', 'name', 'otc', 'phone',)


class PerevalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pereval
        fields = ('title', 'other_title', 'connect', 'add_time',)

