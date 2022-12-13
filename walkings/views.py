from django.shortcuts import render, redirect
from .models import Park, Dog, Dogroup
from .forms import DogroupForm
import json
from pprint import pprint
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from haversine import haversine
from operator import itemgetter
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):

    dogroups = Dogroup.objects.order_by("-pk")

    context = {
        "dogroups": dogroups,
    }

    return render(request, "walkings/index.html", context)


def search(request, x, y):

    latitude = float(x)
    longitude = float(y)

    # 위도는 0.01이, 경도는 0.015가  약 1km에 해당
    # 반경 1km 이내 공원 검색
    condition = Q(latitude__range=(latitude - 0.01, latitude + 0.01)) & Q(
        longitude__range=(longitude - 0.015, longitude + 0.015)
    )

    parks = Park.objects.filter(condition)

    parksJson = []
    for park in parks:

        if not park.parkName.endswith("공원"):
            park.parkName += park.parkType
            park.save()

        distance = round(
            haversine(
                (latitude, longitude),
                (float(park.latitude), float(park.longitude)),
                unit="m",
            )
        )

        temp = {
            "parkName": park.parkName,
            "latitude": park.latitude,
            "longitude": park.longitude,
            "park_pk": park.pk,
            "address": park.address,
            "distance": distance,
        }

        parksJson.append(temp)

    parksJson = sorted(parksJson, key=itemgetter("distance"))

    for p in parksJson:
        if p["distance"] >= 1000:
            p["distance"] = str(round((p["distance"] / 1000), 1)) + "Km"
        else:
            p["distance"] = str(p["distance"]) + "m"

    data = {
        "parksJson": parksJson,
    }
    return JsonResponse(data)


# def test(request):

#     parks = Park.objects.filter(address__icontains="동작구")

#     dogroups = Dogroup.objects.all()

#     park_info = []
#     for park in parks:

#         temp = {
#             "parkName": park.parkName,
#             "latitude": park.latitude,
#             "longitude": park.longitude,
#             "park_pk": park.pk,
#         }

#         park_info.append(temp)

#     parkJson = json.dumps(park_info)
#     context = {
#         "parkJson": parkJson,
#         "dogroups": dogroups,
#     }

#     return render(request, "walkings/test.html", context)


# def create(request, park_pk):

# park = Park.objects.get(pk=park_pk)
# user = request.user
# dog = Dog.objects.get(pk=1)

# if request.method == "POST":
#     dogroup_form = DogroupForm(request.POST)
#     if dogroup_form.is_valid():
#         dogroup = dogroup_form.save(commit=False)
#         dogroup.user = user
#         dogroup.dog = dog
#         dogroup.park = park
#         dogroup.save()
#         dogroup.join.add(request.user)

# dogroup = Dogroup.objects.all()

# dogroup_data = []

# for dogr in dogroup:

#     temp = {
#         "dogroup_pk": dogr.pk,
#         "dogroup_date": dogr.datetime,
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
# return render(request, "walkings/index.html")


@login_required
def create2(request):
    if request.user.is_authenticated:
        park_pk = request.POST["park_pk"]

        park = Park.objects.get(pk=park_pk)
        user = request.user

        if request.method == "POST":
            dogroup_form = DogroupForm(request.POST)
            if dogroup_form.is_valid():
                dogroup = dogroup_form.save(commit=False)
                dogroup.user = user
                dogroup.park = park
                dogroup.save()
                dogroup.join.add(request.user)

        dogroup = Dogroup.objects.all()
    else:
        messages.warning(request, "로그인한 유저만 모임을 개설할 수 있습니다.")

    return redirect("walkings:index")


def detail(request, dogroup_pk):

    dogroup = Dogroup.objects.get(pk=dogroup_pk)

    context = {
        "dogroup": dogroup,
    }
    return render(request, "walkings/detail.html", context)


@login_required
def join(request, dogroup_pk):

    dogroup = Dogroup.objects.get(pk=dogroup_pk)

    if dogroup.user != request.user:
        if dogroup.join.filter(pk=request.user.pk).exists():
            dogroup.join.remove(request.user)
        else:
            dogroup.join.add(request.user)
    return redirect("walkings:index")


@login_required
def delete(request, dogroup_pk):

    dogroup = Dogroup.objects.get(pk=dogroup_pk)

    if dogroup.user == request.user:
        dogroup.delete()
    else:
        messages.warning(request, "본인이 개설한 모임만 삭제 할 수 있습니다.")

    return redirect("walkings:index")


def test2(request):

    dogroups = Dogroup.objects.order_by("-pk")

    context = {
        "dogroups": dogroups,
    }

    return render(request, "walkings/test2.html", context)


def test(request):

    dogroups = Dogroup.objects.order_by("-pk")

    context = {
        "dogroups": dogroups,
    }

    return render(request, "walkings/test.html", context)
