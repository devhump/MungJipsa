from django.shortcuts import render
from .models import Park, Mylotations
from .forms import MylocationForm
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
