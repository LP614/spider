import requests
from lxml import etree
from my_mysql import MyMysql


# 取页面HTML
def get_one_page(url):
    headers = {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        text = response.content.decode('utf-8')
        return text
    return None


def parse_bajia_xpath(html):
    etree_html = etree.HTML(html)
    result = etree_html.xpath('//div[@class="row"]//div[@class="col-xs-12"]/a/@href')
    return result


def main_two():
    url = 'http://www.resgain.net/xmdq.html'
    html = get_one_page(url)
    data = parse_bajia_xpath(html)
    return data


if __name__ == '__main__':
    main_two()