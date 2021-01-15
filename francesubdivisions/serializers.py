from rest_framework import serializers
from francesubdivisions.models import Region, Departement, Epci, Commune, DataYear


class RegionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Region
        fields = ["id", "name", "insee", "siren", "years"]


class DepartementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departement
        depth = 1
        fields = ["id", "name", "insee", "siren", "years", "region"]


class EpciSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Epci
        fields = ["id", "name", "siren", "years"]


class CommuneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Commune
        depth = 2
        fields = [
            "id",
            "name",
            "insee",
            "siren",
            "years",
            "epci",
            "departement",
            "population",
        ]


class DataYearSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DataYear
        fields = ["id", "year"]
