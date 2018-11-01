import json
import requests
import pymysql
from lxml import etree



def get_one_page(url):
    headers = {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        text = response.content.decode('utf-8')
        return text
    return None


def parse_with_xpath(html):
    etree_html = etree.HTML(html)
    # print(etree_html)

    # 匹配所有节点 //*
    # result = etree_html.xpath('//*')
    # print(result)
    # print(len(result))

    # 匹配所有子节点 //a     文本获取：text()
    # result = etree_html.xpath('//a/text()')
    # print(result)

    # 查找元素子节点 /
    # result_article = etree_html.xpath('//div[@class="pic"]/p/text()')  #获取文章
    # print(result_article)0

    from_name = etree_html.xpath('//div[@class="source"]//span[@class="from"]/a/text()')  # 获取名字
    from_address = etree_html.xpath('//div[@class="source"]//span[@class="from"]/a/@href')  # 获取地址

    # 查找元素所有子孙节点 //
    result_title = etree_html.xpath('//div[@class="channel-item"]//h3/a/text()')  # 获取标题
    # print(result_son)

    # 父节点 ..
    # result = etree_html.xpath('//span[@class="pubtime"]/../span/a/text()')
    # print(result)

    # 属性匹配 [@class="xxx"]
    # 文本匹配 text() 获取所有文本//text()
    # result = etree_html.xpath('//div[@class="article"]//text()')
    # print(result)

    # 属性获取 @href
    # result = etree_html.xpath('//div[@class="bd"]/h3/a/@href')
    # print(result)

    # 属性多值匹配 contains(@class 'xx')
    # result = etree_html.xpath('//div[contains(@class, "grid-16-8")]//div[@class="likes"]/text()[1]')
    # print(result)

    # 多属性匹配 or, and, mod, //book | //cd, + - * div = != < > <= >=
    # result = etree_html.xpath('//span[@class="pubtime" and contains(text(), "09-07")]/text()')
    # print(result)

    # 按序选择 [1] [last()] [poistion() < 3] [last() -2]
    # 节点轴
    # //li/ancestor::*  所有祖先节点
    # //li/ancestor::div div这个祖先节点
    # //li/attribute::* attribute轴，获取li节点所有属性值
    # //li/child::a[@href="link1.html"]  child轴，获取直接子节点
    # //li/descendant::span 获取所有span类型的子孙节点
    # //li/following::* 选取文档中当前节点的结束标记之后的所有节点
    # //li/following-sibling::*     选取当前节点之后的所用同级节点


    # 同时取到节点和元素
    # result = etree_html.xpath('//div[@class="channel-item"] | //span[@class="pubtime"]/../span/a/text()')



    # result = etree_html.xpath('//img/attribute::*')
    # print(result)

    # result = etree_html.xpath(
    #     '//div[contains(@class, "channel-group-rec")]//div[@class="title"]/following::*[1]/text()')
    # print(result)
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='spider', charset='utf8')
    cursor = db.cursor()
    # items = []
    for i in range(len(result_title)):
        res_son = {'text': result_title[i].strip(),
                   'from_name': from_name[i].strip(),
                   'from_address': from_address[i].strip()}
        # items.append(res_son)
        sql = 'update into doubantwo(text, from_name, from_address) values("%s", "%s", "%s")' % (res_son['text'], res_son['from_name'], res_son['from_address'])
        cursor.execute(sql)
        db.commit()



def main():
    texts = {}
    for i in range(10):
        url = "https://www.douban.com/group/explore?start=%d" % (i * 30)
        html = get_one_page(url)
    #     title = parse_with_xpath(html)
    #     pages = 'page%d' % (i + 1)
    #     texts[pages] = title
    #     print(pages)
    # str = json.dumps(texts, ensure_ascii=False)
    # with open('text.json', 'w', encoding='utf-8') as f:
    #     f.write(str)
        parse_with_xpath(html)


if __name__ == '__main__':
    main()
