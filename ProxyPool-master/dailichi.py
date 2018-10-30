import requests

PROXY_POOL_URL = 'http://localhost:5555/random'


def get_proxy():
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        return None


if __name__ == '__main__':
    proxy = get_proxy()
    proxies = {
        'http': 'http://' + proxy,
        'https': 'https://' + proxy,
    }
    try:
        response = requests.get('http://httpbin.org/get', proxies=proxies)
        print(response.text)
    except response.exceptions.ConnectionError as e:
        print('Error', e.args)