import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "namung.settings")
django.setup()
from info.models import Hospital

f = open("animal_hospital.csv", "r", encoding="cp949")
rdr = csv.reader(f)
cnt = 0
for line in rdr:
    if line[10] == "정상":
        _name = line[21]
        _phone = line[15]
        if line[18]:
            _address = line[18]
            print(line[18])
        else:
            _address = line[19]
            print(line[19])
        hospital = Hospital(
            name=_name,
            phone=_phone,
            address=_address,
        )
        hospital.save()
    if cnt == 10:
        break
f.close()
