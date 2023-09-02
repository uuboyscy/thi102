import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/Joke/index.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

res = requests.get(url, headers=headers, timeout=60)

# print(res.text)
soup = BeautifulSoup(res.text, "html.parser")  # a = 1; str(a)
# print(soup)

logo_tag_list = soup.findAll("a", {"id": "logo"})  # [<a href="/bbs/" id="logo">批踢踢實業坊</a>]
print(logo_tag_list[0])  # <a href="/bbs/" id="logo">批踢踢實業坊</a>
print(logo_tag_list[0].text)  # 批踢踢實業坊

print("=========")

logo_tag_list = soup.findAll("a", id="logo")
logo_tag_list = soup.find_all("a", id="logo")
print(logo_tag_list[0])  # <a href="/bbs/" id="logo">批踢踢實業坊</a>
print(logo_tag_list[0].text)  # 批踢踢實業坊

print("=========")

print(soup.find("a", id="logo"))  # <a href="/bbs/" id="logo">批踢踢實業坊</a>
print(soup.find("a"))  # <a href="/bbs/" id="logo">批踢踢實業坊</a>
print("https://www.ptt.cc" + soup.find("a", id="logo")["href"])  # /bbs/

print("=========")

logo_tag_list = soup.select("a#logo")  # [<a href="/bbs/" id="logo">批踢踢實業坊</a>]
logo_tag_list = soup.select('a[id="logo"]')  # [<a href="/bbs/" id="logo">批踢踢實業坊</a>]
print(logo_tag_list[0])  # <a href="/bbs/" id="logo">批踢踢實業坊</a>
print(logo_tag_list[0].text)  # 批踢踢實業坊

print("=========")

title_tag = soup.select('div.title')
"""
<div class="title">
<a href="/bbs/joke/M.1693509473.A.93F.html">[耍冷] 我許願</a>
</div>
"""
print(title_tag[0])
title_a_tag = title_tag[0].find("a")  # <a href="/bbs/joke/M.1693509473.A.93F.html">[耍冷] 我許願</a>
print(title_a_tag)
print(title_a_tag.text)

print(soup.select('div[class="title"] a')[0])  # <a href="/bbs/joke/M.1693509473.A.93F.html">[耍冷] 我許願</a>

print(type(soup))
print(type(title_tag[0]))
# print(help(type(soup)))
