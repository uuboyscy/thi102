import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}


def extract_article_content(article_url: str) -> str:
    """
    Do something.

    Example:
     ...
    """
    article_res = requests.get(
        article_url,
        headers=headers,
        timeout=60,
    )

    article_soup = BeautifulSoup(article_res.text, "html.parser")

    main_contain_tag = article_soup.select_one('div[id="main-content"]')

    # main_contain_tag.select('span')[0].extract()
    for span_tag in main_contain_tag.select('span'):
        span_tag.extract()

    return main_contain_tag.text
