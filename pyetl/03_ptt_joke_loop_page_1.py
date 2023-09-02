import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/Joke/index{}.html"

page = 8403

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

for _ in range(5):
    res = requests.get(url.format(page), headers=headers, timeout=60)

    soup = BeautifulSoup(res.text, "html.parser")

    title_tag_list = soup.select('div[class="title"] a')

    for title_tag in title_tag_list:
        title = title_tag.text
        article_url = "https://www.ptt.cc" + title_tag["href"]

        print(title)
        print(article_url)
        print("==========")

    page -= 1
