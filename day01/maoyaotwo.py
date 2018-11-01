
import requests
import re
import json


def get_page(url):
    headers = {
        "User-Agent": "Mozilla/4.0 (compatible;MSIE 7.0; Windows NT 5.1; 360SE)"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.content.decode('utf-8')
    return None


def parse_page(html):
    movies = []
    pattern = re.compile('<p class="star">(.*?)</p>', re.S)
    actors = re.findall(pattern, html)

    pattern = re.compile('movieId.*?>.*?<img.*?<img.*?alt="(.*?)" class.*?', re.S)
    movies_name = re.findall(pattern, html)
    for i in range(len(actors)):
        movies_one = {}
        movies_one['actors'] = actors[i].strip()
        movies_one['movies_name'] = movies_name[i].strip()
        movies.append(movies_one)
    return movies


def main():
    item = {}
    for i in range(10):
        url = "http://maoyan.com/board/4?offset=%d" % i
        html = get_page(url)
        movie = parse_page(html)
        pages = 'page%d' % (i+1)
        item[pages] = movie
        str = json.dumps(item, ensure_ascii=False)
        with open('items.json', 'w', encoding='utf-8')as f:
            f.write(str)


if __name__ == '__main__':
    main()