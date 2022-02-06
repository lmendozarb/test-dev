import factory
from faker import Faker

from adventure import models

faker = Faker('es_ES')

class VehicleTypeFactory(factory.django.DjangoModelFactory):
    name = faker.name()
    max_capacity = faker.random_int(min=1, max=6)


    class Meta:
        model = models.VehicleType

class VehicleFactory(factory.django.DjangoModelFactory):
    name = faker.name()
    passengers = faker.random_int(min=1, max=6)
    vehicle_type = factory.SubFactory(VehicleTypeFactory)
    number_plate = 'AC-12-32'
    fuel_efficiency = faker.pydecimal(4, 2, positive=True, min_value=2000)
    fuel_tank_size = faker.pydecimal(4, 2, positive=True, min_value=2000)

    class Meta:
        model = models.Vehicle


class ServiceAreaFactory(factory.django.DjangoModelFactory):
    kilometer = 500
    gas_price = faker.random_int(min=1, max=100000)

    class Meta:
        model = models.ServiceArea