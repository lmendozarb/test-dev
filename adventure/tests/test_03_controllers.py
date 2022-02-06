import pytest
from rest_framework import status
from rest_framework.test import APITestCase
from django.core import mail

from adventure import models, notifiers, repositories, usecases, views, factories

from .test_02_usecases import MockJourneyRepository

#########
# Tests #
#########


class TestRepository:
    def test_create_vehicle(self, mocker):
        mocker.patch.object(models.Vehicle.objects, "create")
        repo = repositories.JourneyRepository()
        car = models.VehicleType()
        repo.create_vehicle(name="a", passengers=10, vehicle_type=car)
        assert models.Vehicle.objects.create.called


class TestNotifier:
    def test_send_notification(self, mocker):
        mocker.patch.object(mail, "send_mail")
        notifier = notifiers.Notifier()
        notifier.send_notifications(models.Journey())
        assert mail.send_mail.called


class TestCreateVehicleAPIView:
    def test_create(self, client, mocker):
        vehicle_type = models.VehicleType(name="car")
        mocker.patch.object(
            models.VehicleType.objects, "get", return_value=vehicle_type
        )
        mocker.patch.object(
            models.Vehicle.objects,
            "create",
            return_value=models.Vehicle(
                id=1, name="Kitt", passengers=4, vehicle_type=vehicle_type
            ),
        )
        payload = {"name": "Kitt", "passengers": 4, "vehicle_type": "car"}
        response = client.post("/api/adventure/create-vehicle/", payload)
        assert response.status_code == 201

class TestCreateServiceAreaAPIView:
    def test_create(self, client, mocker):
        mocker.patch.object(
            models.ServiceArea.objects,
            "create",
            return_value=models.ServiceArea(
                id=1, kilometer=60, gas_price=784
            ),
        )

        payload = {"kilometer":60, "gas_price":784}
        response = client.post("/api/adventure/create-service-area/", payload)  
        assert response.status_code == 201


@pytest.mark.django_db
class TestGetVehicleView(APITestCase):

    endpoint = '/api/adventure/vehicles/'

    def test_get(self):
        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_by_license_plate(self):
        vehicle = factories.VehicleFactory()
        url = f'{self.endpoint}{vehicle.number_plate}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


@pytest.mark.django_db
class TestGetServiceAreaAPIView(APITestCase):

    endpoint = '/api/adventure/servicearea/'

    def test_get(self):
        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_by_kilometer(self):
        service_area = factories.ServiceAreaFactory()
        url = f'{self.endpoint}{service_area.kilometer}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestStartJourneyAPIView:
    def test_api(self, client, mocker):
        mocker.patch.object(
            views.StartJourneyAPIView,
            "get_repository",
            return_value=MockJourneyRepository(),
        )

        payload = {"name": "Kitt", "passengers": 2}
        response = client.post("/api/adventure/start/", payload)

        assert response.status_code == 201

    def test_api_fail(self, client, mocker):
        mocker.patch.object(
            views.StartJourneyAPIView,
            "get_repository",
            return_value=MockJourneyRepository(),
        )

        payload = {"name": "Kitt", "passengers": 6}
        response = client.post("/api/adventure/start/", payload)

        assert response.status_code == 400