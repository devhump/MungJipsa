from django.shortcuts import render, redirect
from .models import Park, Dog, Dogroup, Mylotations
from .forms import MylocationForm, DogroupForm
import json
from pprint import pprint
import requests

# Create your views here.
def index(request):

    mylocation_form = MylocationForm()

    context = {
        "mylocation_form": mylocation_form,
    }

    return render(request, "walkings/index.html", context)


def test(request):

    parks = Park.objects.filter(address__icontains="동작구")

    park_info = []
    for park in parks:

        temp = {
            "parkName": park.parkName,
            "latitude": park.latitude,
            "longitude": park.longitude,
            "park_pk": park.pk,
        }

        park_info.append(temp)

    parkJson = json.dumps(park_info)
    context = {
        "parkJson": parkJson,
    }

    return render(request, "walkings/test.html", context)


def create(request, park_pk):

    print(request.POST)
    park = Park.objects.get(pk=park_pk)
    user = request.user
    dog = Dog.objects.get(pk=1)

    if request.method == "POST":
        print("실행1")
        dogroup_form = DogroupForm(request.POST)
        print(dogroup_form)
        if dogroup_form.is_valid():
            print("실행2")
            dogroup = dogroup_form.save(commit=False)
            dogroup.user = user
            dogroup.dog = dog
            dogroup.park = park
            dogroup.save()
            return redirect("walkings:test")
    else:
        dogroup_form = DogroupForm()

    dogroup = Dogroup.objects.all()

    dogroup_data = []

    for dogr in dogroup:

        temp = {
            "dogroup_pk": dogr.pk,
            "dogroup_date": dogr.date,
            "dogroup_title": dogr.membercnt,
            "dogroup_dog_pk": dogr.dog_id,
            "dogroup_park_pk": dogr.park_id,
            "dogroup_park_pk": dogr.user_id,
        }

        dogroup_data.append(temp)
    context = {
        "dogroup_data": dogroup_data,
    }

    return render(request, "walkings/create.html", context)
