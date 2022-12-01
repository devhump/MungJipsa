from django.urls import path
from . import views

app_name = "walkings"

urlpatterns = [
    path("", views.index, name="index"),
    path("test/", views.test, name="test"),
    path("create/<int:park_pk>", views.create, name="create"),
    path("detail/<int:dogroup_pk>", views.detail, name="detail"),
]
