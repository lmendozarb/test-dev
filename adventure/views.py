from cgitb import lookup
from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
)
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin

from adventure import models, notifiers, repositories, serializers, usecases


class CreateVehicleAPIView(APIView):
    def post(self, request: Request) -> Response:
        payload = request.data
        vehicle_type = models.VehicleType.objects.get(name=payload["vehicle_type"])
        vehicle = models.Vehicle.objects.create(
            name=payload["name"],
            passengers=payload["passengers"],
            vehicle_type=vehicle_type,
        )
        return Response(
            {
                "id": vehicle.id,
                "name": vehicle.name,
                "passengers": vehicle.passengers,
                "vehicle_type": vehicle.vehicle_type.name,
            },
            status=201,
        )

class CreateServiceAreaAPIView(APIView):
    def post(self, request: Request) -> Response:
        payload = request.data
        left_station = models.ServiceArea.objects.get(pk=payload["left_station"]) if "left_station" in payload else None
        right_station = models.ServiceArea.objects.get(pk=payload["right_station"]) if "right_station" in payload else None
        service_area = models.ServiceArea.objects.create(
            kilometer=payload["kilometer"],
            gas_price=payload["gas_price"],
            left_station=left_station,
            right_station=right_station
        )

        return Response(
            {
                "id": service_area.id,
                "kilometer": service_area.kilometer,
                "gas_price": service_area.gas_price,
                "left_station": service_area.left_station,
                "right_station": service_area.right_station
            },
            status=201
        )

class StartJourneyAPIView(generics.CreateAPIView):
    serializer_class = serializers.JourneySerializer

    def perform_create(self, serializer) -> None:
        repo = self.get_repository()
        notifier = notifiers.Notifier()
        usecase = usecases.StartJourney(repo, notifier).set_params(
            serializer.validated_data
        )
        try:
            usecase.execute()
        except usecases.StartJourney.CantStart as e:
            raise ValidationError({"detail": str(e)})

    def get_repository(self) -> repositories.JourneyRepository:
        return repositories.JourneyRepository()


@extend_schema_view(
    list=extend_schema(
        summary='List all Vehicles',
        description='Return a list of all vehicles in the system.',
        tags=['Vehicles'],
    ),
    retrieve=extend_schema(
        summary='Retrieve Vehicles',
        description='Get vehicle to number plate',
        tags=['Vehicles'],
    ),
)
class FullVehicleList(viewsets.GenericViewSet, RetrieveModelMixin, ListModelMixin):
    queryset = models.Vehicle.objects.all()
    serializer_class = serializers.VehicleSerializer
    lookup_field = "number_plate"


@extend_schema_view(
    list=extend_schema(
        summary='List all Service Area',
        description='Return a list of all ServiceArea in the system.',
        tags=['Service Area'],
    ),
    retrieve=extend_schema(
        summary='Retrieve Service Area',
        description='Get Service Area to kilometer',
        tags=['Service Area'],
    ),
)
class ServiceAreaList(viewsets.GenericViewSet, RetrieveModelMixin, ListModelMixin):
    queryset = models.ServiceArea.objects.all()
    serializer_class = serializers.ServiceAreaSerializer
    lookup_field = "kilometer"


@extend_schema_view(
    create=extend_schema(
        summary='Create Service Area',
        description='Create a service are',
        tags=['Service Area'],
    ),
)
class CreateServiceAreaView(viewsets.GenericViewSet, CreateModelMixin):
    queryset = models.ServiceArea.objects.all()
    serializer_class = serializers.CreateServiceAreaSerializer
    lookup_field = "kilometer"