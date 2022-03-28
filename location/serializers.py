from rest_framework import serializers

from . import models


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.City
        fields = ['title']


class ProvinceSerializer(serializers.ModelSerializer):
    cities = CitySerializer(source='city_set', many=True, read_only=True)

    class Meta:
        model = models.Province
        fields = [
            'title',
            'cities',
        ]
