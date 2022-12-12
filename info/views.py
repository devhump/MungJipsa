from django.shortcuts import render, redirect
from .models import Hospital, Deserted, PetPlace, PetPlaceSlideImage, PetPlaceBodyImage
from django.core.paginator import Paginator
from django.db.models import Q
from .serializer import PlaceSerializer

# Create your views here.
def hospital(request):
    hospitals = Hospital.objects.all()
    search = request.GET.get("search")
    areaSearch = request.GET.get("areaSearch")
    if not areaSearch:
        areaSearch = "전국"
    if areaSearch == "전국":
        areaSearch = ""

    if search:
        hospitals = hospitals.filter(
            Q(name__icontains=search) | Q(address__icontains=search)
        )
        hospitals = hospitals.filter(Q(address__icontains=areaSearch))
    else:
        search = ""
        hospitals = hospitals.filter(Q(address__icontains=areaSearch))
    paginator = Paginator(hospitals, 12)
    page = request.GET.get("page")
    posts = paginator.get_page(page)

    context = {
        "searchval": search,
        "areaval": areaSearch,
        "hospitals": hospitals,
        "posts": posts,
        "paginator": paginator,
    }

    if page:
        leftIndex = int(page) - 3
        if leftIndex < 1:
            leftIndex = 1

        rightIndex = int(page) + 3
        if rightIndex > paginator.num_pages:
            rightIndex = paginator.num_pages

        custom_range = range(leftIndex, rightIndex + 1)

        context = {
            "searchval": search,
            "areaval": areaSearch,
            "hospitals": hospitals,
            "posts": posts,
            "paginator": paginator,
            "custom_range": custom_range,
        }

    return render(request, "info/hospital.html", context)


from datetime import date


def deserted(request):
    animals = Deserted.objects.all()
    today = date.today()
    animals = animals.filter(noticeEdt__gte=today)
    search = request.GET.get("search")
    areaSearch = request.GET.get("areaSearch")
    if not areaSearch:
        areaSearch = "전국"
    if areaSearch == "전국":
        areaSearch = ""

    if search:
        animals = animals.filter(
            Q(kindCd__icontains=search) | Q(careAddr__icontains=search)
        )
        animals = animals.filter(Q(careAddr__icontains=areaSearch))
    else:
        search = ""
        animals = animals.filter(Q(careAddr__icontains=areaSearch))
    paginator = Paginator(animals, 12)
    page = request.GET.get("page")
    posts = paginator.get_page(page)

    context = {
        "searchval": search,
        "areaval": areaSearch,
        "animals": animals,
        "posts": posts,
        "paginator": paginator,
    }

    if page:
        leftIndex = int(page) - 3
        if leftIndex < 1:
            leftIndex = 1

        rightIndex = int(page) + 3
        if rightIndex > paginator.num_pages:
            rightIndex = paginator.num_pages

        custom_range = range(leftIndex, rightIndex + 1)

        context = {
            "searchval": search,
            "areaval": areaSearch,
            "animals": animals,
            "posts": posts,
            "paginator": paginator,
            "custom_range": custom_range,
        }

    return render(request, "info/deserted_index.html", context)


def deserted_detail(request, pk):
    animal = Deserted.objects.get(pk=pk)
    context = {"animal": animal}
    return render(request, "info/deserted_detail.html", context)


from rest_framework.viewsets import ModelViewSet


class PlaceViewSet(ModelViewSet):
    queryset = PetPlace.objects.all()
    serializer_class = PlaceSerializer


def place(request):
    places = PetPlace.objects.all()

    search = request.GET.get("search")
    areaSearch = request.GET.get("areaSearch")
    if not areaSearch:
        areaSearch = "전국"
    if areaSearch == "전국":
        areaSearch = ""

    if search:
        places = places.filter(Q(name__icontains=search) | Q(address__icontains=search))
        places = places.filter(Q(address__icontains=areaSearch))
    else:
        search = ""
        places = places.filter(Q(address__icontains=areaSearch))
    paginator = Paginator(places, 12)
    page = request.GET.get("page")
    posts = paginator.get_page(page)

    context = {
        "searchval": search,
        "areaval": areaSearch,
        "places": places,
        "posts": posts,
        "paginator": paginator,
    }

    if page:
        leftIndex = int(page) - 3
        if leftIndex < 1:
            leftIndex = 1

        rightIndex = int(page) + 3
        if rightIndex > paginator.num_pages:
            rightIndex = paginator.num_pages

        custom_range = range(leftIndex, rightIndex + 1)

        context = {
            "searchval": search,
            "areaval": areaSearch,
            "animals": places,
            "posts": posts,
            "paginator": paginator,
            "custom_range": custom_range,
        }

    return render(request, "info/place_index.html", context)


import random


def place_detail(request, pk):
    place = PetPlace.objects.get(pk=pk)
    slideimages = PetPlaceSlideImage.objects.filter(petplace_id=pk)
    bodyimages = PetPlaceBodyImage.objects.filter(petplace_id=pk)
    num = random.randrange(1, 7)
    lst = ["1.png", "2.png", "3.png", "4.png", "5.png", "6.png"]
    photo = lst[num - 1]
    banner = "../../static/images/" + photo

    context = {
        "place": place,
        "slideimages": slideimages,
        "bodyimages": bodyimages,
        "banner": banner,
    }
    return render(request, "info/place_detail.html", context)
