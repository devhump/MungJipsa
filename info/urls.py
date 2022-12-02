from django.urls import path
from . import views

app_name = "info"

urlpatterns = [
    path("hospital/", views.hospital, name="hospital"),
    path("deserted/", views.deserted, name="deserted"),
    path("deserted/<int:pk>", views.deserted_detail, name="deserted_detail"),
]
