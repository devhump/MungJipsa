from django.shortcuts import render, redirect
from .models import Park, Dog, Dogroup, Mylotations
from .forms import MylocationForm, DogroupForm
import json
from pprint import pprint
from django.http import JsonResponse


# Create your views here.
def index(request):

    mylocation_form = MylocationForm()

    context = {
        "mylocation_form": mylocation_form,
    }

    return render(request, "walkings/index.html", context)


def test(request):

    parks = Park.objects.filter(address__icontains="동작구")

    dogroups = Dogroup.objects.all()
    user_dogs = Dog.objects.filter(user=request.user)

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
        "dogroups": dogroups,
        "user_dogs": user_dogs,
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

    # dogroup = Dogroup.objects.all()

    # dogroup_data = []

    # for dogr in dogroup:

    #     temp = {
    #         "dogroup_pk": dogr.pk,
    #         "dogroup_date": dogr.date,
    #         "dogroup_title": dogr.membercnt,
    #         "dogroup_dog_pk": dogr.dog.pk,
    #         "dogroup_park_pk": dogr.park.pk,
    #         "dogroup_park_pk": dogr.user.pk,
    #     }

    #     dogroup_data.append(temp)
    # print(dogroup_data)
    # context = {
    #     "dogroup_data": dogroup_data,
    # }

    # return JsonResponse(context)
    return redirect("walkings:test")


def detail(request, dogroup_pk):

    dogroup = Dogroup.objects.get(pk=dogroup_pk)

    context = {
        "dogroup": dogroup,
    }
    return render(request, "walkings/detail.html", context)
