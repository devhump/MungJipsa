from django.shortcuts import render
import random

# Create your views here.


def main(request):
    num = random.randrange(1, 7)
    lst = ["1.png", "2.png", "3.png", "4.png", "5.png", "6.png"]
    photo = lst[num - 1]
    address = "../../static/images/" + photo
    context = {"banner": address}
    return render(request, "main/main.html", context)
