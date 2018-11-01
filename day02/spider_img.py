import pymysql
import requests
from lxml import etree

def get_one_page(url):
    headers = {
        "User-Agent": "Mozilla/4.0 (compatible;MSIE 7.0; Windows NT 5.1; 360SE)"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.content.decode('utf-8')
    return None


def parse_page(html):
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='spider', charset='utf8')
    cursor = db.cursor()
    etree_html = etree.HTML(html)
    name = etree_html.xpath('//div[@class="movie-item-info"]//p[@class="name"]/a/text()')
    actor = etree_html.xpath('//div[@class="movie-item-info"]//p[@class="star"]/text()')
    releasetime = etree_html.xpath('//div[@class="movie-item-info"]//p[@class="releasetime"]/text()')
    images = etree_html.xpath('//dl[@class="board-wrapper"]//a[@class="image-link"]//img[@class="board-img"]/@data-src')
    image_name = []
    for img in images:
        arr = img.split('@')
        filname = arr[0].split('/')[-1]
        image_name.append(filname)
    for i in range(len(name)):
        # items = {'name': name[i].strip(),
        #          'actor': actor[i].strip(),
        #          'releasetime': releasetime[i].strip(),
        #          'image': image_name[i]
        #          }
        # sql = 'insert into maoyantwo(name, actor, time, image) values("%s", "%s", "%s", "%s")' % (items['name'], items['actor'], items['releasetime'], items['image'])
        sql = 'insert into maoyantwo(name, actor, time, image) values("%s", "%s", "%s", "%s")' % (name[i].strip(), actor[i].strip(), releasetime[i].strip(), image_name[i])
        cursor.execute(sql)
        db.commit()


def main():
    url = "http://maoyan.com/board"
    html = get_one_page(url)
    parse_page(html)


if __name__ == '__main__':
    main()
