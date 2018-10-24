import requests
import re
import json

def get_page(url):
    headers = {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # return response.text   字符串
        return response.content.decode('utf-8') #字节流
    return None


def parse_page(html):
    # 爬去电影主演名字
    pattern = re.compile('<p class="star">(.*?)</p>', re.S)
    actor_items = re.findall(pattern, html)

    # 爬去电影名字
    pattern = re.compile('movieId.*?>.*?<img.*?<img.*?alt="(.*?)" class.*?', re.S)
    movie_items = re.findall(pattern, html)
    # # 爬去电影时间
    # # pattern = re.compile('</p>.*?releasetime.*?>(.*?)</p>', re.S)
    # # pattern = re.compile('</i>.*?board-index.*?>(.*?)</i>', re.S)
    # # 爬去图片地址
    # # pattern = re.compile('</dd>.*?board-index.*?<img.*?<img.*?src="(.*?)".*?</a>', re.S)
    # items = re.findall(pattern, html)
    # return items
    movies = []
    for i in range(len(actor_items)):
        one_movie = {}
        one_movie['actors']=actor_items[i].strip()
        one_movie['movie_name']=movie_items[i].strip()
        movies.append(one_movie)
    return movies


def write_img(url):
    arr = url.split('@')
    filename = arr[0].split('/')[-1]
    with open('./images/%s' % filename, 'wb') as f:
        response = requests.get(url)
        f.write(response.content)


def main():
    items={}
    for i in range(10):
        url = "http://maoyan.com/board/4?offset=%d" % (i*10)
        html = get_page(url)
        movies = parse_page(html)
        page_name = 'page%d' % (i+1)
        items[page_name] = movies
        str = json.dumps(items, ensure_ascii=False)
    with open('text.json', 'w', encoding='utf-8') as f:
        f.write(str)
        # print(html)
        # for item in items:
        #     print(item.strip())
        #     # write_img(item.strip())
        write_img()

if __name__ == '__main__':
    main()
