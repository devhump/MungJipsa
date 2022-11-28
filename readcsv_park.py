import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "namung.settings")
django.setup()
from walkings.models import Park

f = open("park.csv", "r", encoding="cp949")
rdr = csv.reader(f)
cnt = 0
for line in rdr:
    if line[5]:
        _manageNo = line[0]
        _parkName = line[1]
        _parkType = line[2]
        if line[4]:
            _address = line[4]
        else:
            _address = line[3]
        _latitude = line[5]
        _longitude = line[6]
        _size = line[7]
        park = Park(
            manageNo=_manageNo,
            parkName=_parkName,
            parkType=_parkType,
            address=_address,
            latitude=_latitude,
            longitude=_longitude,
            size=_size,
        )
        park.save()

    print(_parkName)
    if cnt == 10:
        break
f.close()
