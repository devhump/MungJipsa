import requests

url = "http://api.data.go.kr/openapi/tn_pubr_public_cty_park_info_api"
params = {
    "serviceKey": "d86ISPyRZPJgxIR2COTeScPuLOmAwSAcx0AAhXehnirErwVab/Cl9JUQSziO3E+EJhj4XX+Kl03NXnHay2Pa2A==",
    "pageNo": "0",
    "numOfRows": "100",
    "type": "xml",
    "manageNo": "",
    "parkNm": "",
    "parkSe": "",
    "rdnmadr": "",
    "lnmadr": "",
    "latitude": "",
    "longitude": "",
    "parkAr": "",
    "mvmFclty": "",
    "amsmtFclty": "",
    "cnvnncFclty": "",
    "cltrFclty": "",
    "etcFclty": "",
    "appnNtfcDate": "",
    "institutionNm": "",
    "phoneNumber": "",
    "referenceDate": "",
    "instt_code": "",
}
response = requests.get(url, params=params)
print(response.content)
