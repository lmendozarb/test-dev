from django.urls import path, include
from rest_framework.routers import SimpleRouter

from adventure import views

router = SimpleRouter()
router.register('vehicles', views.FullVehicleList)
router.register('servicearea', views.ServiceAreaList)
router.register('create-servicearea', views.CreateServiceAreaView)

urlpatterns = [
    path('', include(router.urls)),
    path("create-vehicle/", views.CreateVehicleAPIView.as_view()),
    path("create-service-area/", views.CreateServiceAreaAPIView.as_view()),
    path("start/", views.StartJourneyAPIView.as_view()),
]
