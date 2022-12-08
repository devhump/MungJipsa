from django.shortcuts import render
import random

# Create your views here.


def main(request):
    num = random.randrange(1, 6)
    lst1 = ["P1.png", "P2.png", "P3.png", "P4.png", "P5.png"]
    below = lst1[num - 1]
    place = "../../static/images/" + below
    num2 = random.randrange(1, 6)
    lst2 = ["D1.png", "D2.png", "D3.png", "D4.png", "D5.png"]
    photo = lst2[num2 - 1]
    address = "../../static/images/" + photo
    num3 = random.randrange(1, 6)
    lst3 = ["H1.png", "H2.png", "H3.png", "H4.png", "H5.png"]
    hospital = lst3[num3 - 1]
    sub = "../../static/images/" + hospital
    context = {"aside2": address, "aside1": sub, "banner": place}
    return render(request, "main/main.html", context)
