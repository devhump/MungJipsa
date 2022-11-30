from django.shortcuts import render, redirect
from .models import Hospital, Deserted
from django.core.paginator import Paginator

# Create your views here.
def hospital(request):
    hospitals = Hospital.objects.all()
    paginator = Paginator(hospitals, 12)
    page = request.GET.get("page")
    posts = paginator.get_page(page)

    leftIndex = int(page) - 3
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = int(page) + 3
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages

    custom_range = range(leftIndex, rightIndex + 1)

    context = {
        "hospitals": hospitals,
        "posts": posts,
        "paginator": paginator,
        "custom_range": custom_range,
    }
    return render(request, "info/hospital.html", context)
