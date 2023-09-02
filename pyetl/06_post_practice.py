import requests

url = "http://httpbin.org/post?a=123"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

form_data = {
    "username": "test"
}

json_data = {
    "test": ["a", "b", "c"]
}

res = requests.post(url, headers=headers, data=form_data, json=json_data)

print(res.text)
