import os

import requests
from bs4 import BeautifulSoup

from common_util import extract_article_content

if not os.path.exists("./joke"):
    os.mkdir("./joke")

url = "https://www.ptt.cc/bbs/Joke/index.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

for _ in range(5):
    res = requests.get(url, headers=headers, timeout=60)

    soup = BeautifulSoup(res.text, "html.parser")

    title_tag_list = soup.select('div[class="title"] a')

    for title_tag in title_tag_list:
        title = title_tag.text
        article_url = "https://www.ptt.cc" + title_tag["href"]

        article_content = extract_article_content(article_url)

        ############# Load file ##############
        file_name = title
        try:
            with open(f"./joke/{file_name}.txt", "w", encoding="utf-8") as f:
                f.write(article_content)
        except FileNotFoundError as e:
            print(e.args)
            file_name = file_name.replace("/", " ")
        except OSError as e:
            print(e.args)
        ################################################

        print(title)
        print(article_url)
        print("==========")

    url = "https://www.ptt.cc" + soup.select('a[class="btn wide"]')[1]["href"]
