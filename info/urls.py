from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = "info"

router = DefaultRouter()
router.register("places", views.PlaceViewSet)

urlpatterns = [
    path("hospital/", views.hospital, name="hospital"),
    path("deserted/", views.deserted, name="deserted"),
    path("deserted/<int:pk>", views.deserted_detail, name="deserted_detail"),
    path("place/", views.place, name="place"),
    path("", include(router.urls)),
]
