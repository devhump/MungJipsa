from django.shortcuts import render, redirect
from .models import Hospital, Deserted
from django.core.paginator import Paginator

# Create your views here.
def hospital(request):
    hospitals = Hospital.objects.all()
    paginator = Paginator(hospitals, 12)
    page = request.GET.get("page")
    posts = paginator.get_page(page)
    context = {
        "hospitals": hospitals,
        "posts": posts,
        "paginator": paginator,
    }
    return render(request, "info/hospital.html", context)
