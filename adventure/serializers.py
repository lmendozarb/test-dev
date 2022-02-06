from statistics import mode
from rest_framework import serializers

from adventure import models


class JourneySerializer(serializers.Serializer):
    name = serializers.CharField()
    passengers = serializers.IntegerField()


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vehicle
        fields = [
            "name",
            "passengers",
            "vehicle_type",
            "number_plate",
        ]


class ServiceAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ServiceArea
        fields = '__all__'


class CreateServiceAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ServiceArea
        fields = [
            "kilometer",
            "gas_price"
        ]