import requests
from bs4 import BeautifulSoup

url = "https://organic.afa.gov.tw/InOrganic/QueryApplyList"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36"
}

data = {
    "TYPE": "1",
    "YEAR": "111",
    "qNnify_NO": "",
    "qC_NAME": "",
    "qPaper_NO": "",
    "qProduct_NAME": "米".encode("big5"),
    "B": "查　　詢"
}

res = requests.post(url, headers=headers, data=data)
print(res.text)