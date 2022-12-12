import requests
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import json
import django
from datetime import date

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "namung.settings")
django.setup()
from info.models import Deserted

# 유기견 db
#################################################
# 필수 값
#################################################

# .env 파일의 api 불러옴
load_dotenv()
API_SECRET_KEY = os.getenv("API_SECRET_KEY")


# 축종 (개)
upkind = "&upkind=" + "417000"
# 검색 시작일
today = date.today()
bgnde = "&bgnde=" + str(today.strftime("%Y%m%d"))
# 현재페이지
numpage = 1
cpage = "&pageNo=" + str(numpage)
# 페이지당 목록 수
numrows = 1000
rows = "&numOfRows=" + str(numrows)
_type = "&_type=" + "json"


#################################################
# 선택 값
#################################################


def get_list():
    URL = (
        "https://apis.data.go.kr/1543061/abandonmentPublicSrvc/abandonmentPublic?serviceKey="
        + API_SECRET_KEY
        + bgnde
        + upkind
        + cpage
        + rows
        + _type
    )

    print(URL)

    response = requests.get(URL, verify=False)
    print(URL)
    print(response.status_code)
    jsonresponse = response.json()
    for i in range(numrows):
        _kindCd = jsonresponse["response"]["body"]["items"]["item"][i]["kindCd"]
        _colorCd = jsonresponse["response"]["body"]["items"]["item"][i]["colorCd"]
        _age = jsonresponse["response"]["body"]["items"]["item"][i]["age"]
        _weight = jsonresponse["response"]["body"]["items"]["item"][i]["weight"]
        _happenDt = jsonresponse["response"]["body"]["items"]["item"][i]["happenDt"]
        _happenPlace = jsonresponse["response"]["body"]["items"]["item"][i][
            "happenPlace"
        ]
        _noticeSdt = jsonresponse["response"]["body"]["items"]["item"][i]["noticeSdt"]
        _noticeEdt = jsonresponse["response"]["body"]["items"]["item"][i]["noticeEdt"]
        _processState = jsonresponse["response"]["body"]["items"]["item"][i][
            "processState"
        ]
        _sexCd = jsonresponse["response"]["body"]["items"]["item"][i]["sexCd"]
        _neuterYn = jsonresponse["response"]["body"]["items"]["item"][i]["neuterYn"]
        _specialMark = jsonresponse["response"]["body"]["items"]["item"][i][
            "specialMark"
        ]
        _careNm = jsonresponse["response"]["body"]["items"]["item"][i]["careNm"]
        _careTel = jsonresponse["response"]["body"]["items"]["item"][i]["careTel"]
        _careAddr = jsonresponse["response"]["body"]["items"]["item"][i]["careAddr"]
        _imageURL = jsonresponse["response"]["body"]["items"]["item"][i]["popfile"]

        d_happenDt = date(int(_happenDt[0:4]), int(_happenDt[4:6]), int(_happenDt[6:]))
        d_noticeSdt = date(
            int(_noticeSdt[0:4]), int(_noticeSdt[4:6]), int(_noticeSdt[6:])
        )
        d_noticeEdt = date(
            int(_noticeEdt[0:4]), int(_noticeEdt[4:6]), int(_noticeEdt[6:])
        )

        deserted = Deserted(
            kindCd=_kindCd,
            colorCd=_colorCd,
            age=_age,
            weight=_weight,
            happenDt=d_happenDt,
            happenPlace=_happenPlace,
            noticeSdt=d_noticeSdt,
            noticeEdt=d_noticeEdt,
            processState=_processState,
            sexCd=_sexCd,
            neuterYn=_neuterYn,
            specialMark=_specialMark,
            careNm=_careNm,
            careTel=_careTel,
            careAddr=_careAddr,
            imageURL=_imageURL,
        )
        deserted.save()


get_list()
