from django.urls import path
from django.conf.urls import url
from . import views

app_name = "schedules"

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
]