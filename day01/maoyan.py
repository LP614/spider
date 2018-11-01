
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
    # 爬取电影主演名字：
    pattern = re.compile('<p class="star">(.*?)</p>', re.S)
    actor_items = re.findall(pattern, html)

    # 爬取电影名字
    pattern = re.compile('movieId.*?>.*?<img.*?<img.*?alt="(.*?)" class.*?', re.S)
    movie_items = re.findall(pattern, html)

    # 爬取电影上映时间
    pattern = re.compile('</p>.*?releasetime.*?>(.*?)</p>', re.S)
    movie_time = re.findall(pattern, html)
    movies = []
    for i in range(len(actor_items)):
        one_movie = {}
        one_movie['actor'] = actor_items[i].strip()
        one_movie['name'] = movie_items[i].strip()
        one_movie['time'] = movie_time[i].strip()
        movies.append(one_movie)
    return movies


def write_img(url):
    arr = url.split('@')
    filname = arr[0].split('/')[-1]
    with open('./images/%s' % filname, 'wb')as f:
        response = requests.get(url)
        f.write(response.content)


def main():
    items = {}
    for i in range(10):
        url = "http://maoyan.com/board/4?offset=%d" % (i*10)
        html = get_page(url)
        movies = parse_page(html)
        page_name = 'page%d' % (i+1)
        items[page_name] = movies
        str = json.dumps(items, ensure_ascii=False)
    with open('textone.json', 'w', encoding='utf-8') as f:
        f.write(str)


if __name__ == '__main__':
    main()