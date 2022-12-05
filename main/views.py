from django.shortcuts import render
import random

# Create your views here.


def main(request):
    num = random.randrange(1, 7)
    lst = ["1.png", "2.png", "3.png", "4.png", "5.png", "6.png"]
    photo = lst[num - 1]
    address = "../../static/images/" + photo
    num2 = random.randrange(1, 6)
    lst2 = ["01.png", "02.png", "03.png", "04.png", "05.png"]
    hospital = lst2[num2 - 1]
    sub = "../../static/images/" + hospital
    context = {"banner": address, "aside": sub}
    return render(request, "main/main.html", context)
