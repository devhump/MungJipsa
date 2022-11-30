from django.shortcuts import render, redirect
from .models import Park, Dog, Dogroup, Mylotations
from .forms import MylocationForm, DogroupForm
import json
from pprint import pprint

# Create your views here.
def index(request):

    mylocation_form = MylocationForm()

    context = {
        "mylocation_form": mylocation_form,
    }

    return render(request, "walkings/index.html", context)


def test(request):

    parks = Park.objects.filter(address__icontains="동작구")

    print(len(parks))
    park_info = []
    for park in parks:

        temp = {
            "parkName": park.parkName,
            "latitude": park.latitude,
            "longitude": park.longitude,
            "park_pk": park.pk,
        }

        park_info.append(temp)

    pprint(park_info)
    parkJson = json.dumps(park_info)
    context = {
        "parkJson": parkJson,
    }

    return render(request, "walkings/test.html", context)


def create(request):

    park = Park.objects.get(pk=2)
    user = request.user
    dog = Dog.objects.get(pk=1)

    if request.method == "POST":
        dogroup_form = DogroupForm(request.POST)
        if dogroup_form.is_valid():
            dogroup = dogroup_form.save(commit=False)
            dogroup.user = user
            dogroup.dog = request.user.dog
            dogroup.park = park
            dogroup.save()
            return redirect("walking:index")
    else:
        dogroup_form = DogroupForm()

    context = {
        "dogroup_form": dogroup_form,
    }

    return render(request, "walkings/create.html", context)
