import requests
import os
from bs4 import BeautifulSoup as bs
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "namung.settings")
django.setup()

idx = 113
while idx < 114:
    url = (
        "http://hatdog.co.kr/pc_hatdog/?m1Code=ar_info&m2Code=ar_info&mode=view&idx="
        + str(idx)
    )

    response = requests.get(url)

    soup = bs(response.text, "html.parser")

    print(response.status_code)
    basic = soup.select("li > dl > dd")
    for i in range(3):
        print(basic[i].text)
    images = soup.select("p.swiper-slide img")
    for image in images:
        print(image.attrs["src"])
    idx += 1
