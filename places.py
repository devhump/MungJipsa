import requests
import os
from bs4 import BeautifulSoup as bs
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "namung.settings")
django.setup()

from info.models import PetPlace, PetPlaceSlideImage, PetPlaceBodyImage

# idx range: 76 - 11503

idx = 83
while idx < 11505:
    url = (
        "http://hatdog.co.kr/pc_hatdog/?m1Code=ar_info&m2Code=ar_info&mode=view&idx="
        + str(idx)
    )

    response = requests.get(url)

    soup = bs(response.text, "html.parser")

    if response.status_code == 200 and soup.select("div.sContainer"):
        try:
            _name = soup.select_one("p.swiper-slide img").attrs["alt"]
        except:
            print(idx, "문제가 있는 페이지. 다음으로 넘어갑니다.")
            idx += 1
            continue

        basic = soup.select("li > dl > dd")
        _petplace = PetPlace(
            name=_name,
            address=basic[0].text,
            tel=basic[1].text,
            url=basic[2].text,
        )
        _petplace.save()

        slideimages = soup.select("p.swiper-slide img")
        for image in slideimages:
            _slideimage = PetPlaceSlideImage(
                petplace=_petplace,
                slideimage=image.attrs["src"],
            )
            _slideimage.save()

        bodyimages = soup.select("div.s21_tabcontent_left img")
        for image in bodyimages:
            _bodyimage = PetPlaceBodyImage(
                petplace=_petplace, bodyimage=image.attrs["src"]
            )
            _bodyimage.save()

        print(idx, "done")
    else:
        print(idx, "not available")

    idx += 1
