from django.urls import path
from . import views

app_name = "walkings"

urlpatterns = [
    path("", views.index, name="index"),
    path("test/", views.test, name="test"),
    # path("create/<int:park_pk>", views.create, name="create"),
    path("detail/<int:dogroup_pk>", views.detail, name="detail"),
    path("join/<int:dogroup_pk>", views.join, name="join"),
    path("delete/<int:dogroup_pk>", views.delete, name="delete"),
    path("search/<x>/<y>/", views.search, name="search"),
    path("create2/", views.create2, name="create2"),
]
