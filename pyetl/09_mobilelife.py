import json

import requests

url = "https://www.newmobilelife.com/wp-json/csco/v1/more-posts"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36"
}

data_str = """action: csco_ajax_load_more
page: 3
posts_per_page: 30"""

data = {row.split(": ")[0]: row.split(": ")[1] for row in data_str.split("\n")}

data = {}
for row in data_str.split("\n"):
    data[row.split(": ")[0]] = row.split(": ")[1]

print(data)

res = requests.post(url, headers=headers, data=data)
# print(res.text)
json_data = json.loads(res.text)
# print(json.loads(res.text))

print(json_data.keys())
print(json_data["success"])
