import requests
from bs4 import BeautifulSoup

article_url = "https://www.ptt.cc/bbs/joke/M.1693524684.A.F7E.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

article_res = requests.get(article_url, headers=headers)

article_soup = BeautifulSoup(article_res.text, "html.parser")

main_contain_tag = article_soup.select_one('div[id="main-content"]')

# main_contain_tag.select('span')[0].extract()
for span_tag in main_contain_tag.select('span'):
    span_tag.extract()

# print(main_contain_tag.select('span'))  # <span class="article-meta-tag">作者</span>

print(main_contain_tag.text)

