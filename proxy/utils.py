import requests


def get_page(url):
    headers = {
        "User-Agent": "Mozilla/4.0 (compatible;MSIE 7.0; Windows NT 5.1; 360SE)"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.content.decode('utf-8')