from bs4 import BeautifulSoup
import requests
import pymysql

def get_one_page(url):
    headers = {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        text = response.content.decode('utf-8')
        return text
    return None


def parse_soup(html):
    soup = BeautifulSoup(html, 'lxml')
    # print(soup.prettify())   #取网页缩进格式输出
    # print(soup.text.title())  #去网页title内容
    # print(soup.head)
    # print(soup.p)   #拿到遇到的第一个p标签
    print(soup.a.attrs["href"])


def main():
    url = "http://image.so.com/i?src=360pic_strong&z=1&i=0&cmg=84e505caa342e6f9c7bd596602f32f56&q=%E7%BE%8E%E5%A5%B3%E5%9B%BE%E7%89%87"
    html = get_one_page(url)
    parse_soup(html)


if __name__ == '__main__':
    main()