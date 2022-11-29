import requests
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "namung.settings")
django.setup()
from info.models import Deserted


#################################################
# 필수 값
#################################################

# .env 파일의 api 불러옴
load_dotenv()
API_SECRET_KEY = os.getenv("API_SECRET_KEY")

# 축종 (개)
upkind = "&upkind=" + "417000"
# 현재페이지
cpage = "&pageNo=" + "1"
# 페이지당 목록 수
rows = "&numOfRows=" + "10"


#################################################
# 선택 값
#################################################


def get_list():
    URL = (
        "https://apis.data.go.kr/1543061/abandonmentPublicSrvc/abandonmentPublic?serviceKey="
        + API_SECRET_KEY
        + upkind
        + cpage
        + rows
    )

    print(URL)

    response = requests.get(URL)
    # print(URL)
    # print(response.status_code)

    soup = BeautifulSoup(response.text, "xml")  # xml 문서라서
    items = soup.find_all("desertionNo")

    print(items)

    return items


get_list()
