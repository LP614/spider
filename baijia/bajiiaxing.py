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


def parse_bajia_xpath():
    etree_html = etree.HTML()
    result = etree_html.xpath('//div[@class="row"]//div[@class="col-xs-12"]/a/@href')
    return result


def parse_with_xpath(html):
    etree_html = etree.HTML(html)
    result = etree_html.xpath('//div[@class="row"]//div[@class="col-xs-12"]/a/text()')
    return result


def main():
    names = ['zhao', 'qian', 'sun', 'li', 'zhou', 'wu', 'zheng', 'wang', 'feng', 'chen',
             'chu', 'wei', 'jiang', 'shen', 'han', 'yang', 'zhu', 'qin', 'you', 'xu', 'ho',
             'lu', 'shi', 'zhang', 'kong', 'tzao', 'yan', 'hua', 'jin', 'wei1', 'tao', 'jiang1',
             'qi', 'xie', 'zou', 'yu', 'bai', 'shui', 'dou', 'zhang1', 'yun', 'su', 'pan', 'ge',
             'xi', 'fan', 'peng', 'lang', 'lu1', 'wei2', 'chang', 'ma', 'miao', 'feng1', 'hua1',
             'fang', 'yu1', 'ren', 'yuan', 'liu', 'feng2', 'bao', 'shi1', 'tang', 'fei', 'lian',
             'cen', 'xue', 'lei', 'he', 'ni', 'tang1', 'teng', 'yin', 'lo', 'bi', 'hao', 'wu1',
             'an', 'chang1', 'yue', 'yu2', 'shi2', 'fu', 'pi', 'bian', 'qi1', 'kang', 'wu2', 'yu3',
             'yuan1', 'bu', 'gu', 'meng', 'ping', 'huang', 'he1', 'mu', 'xiao',
             'yin1', 'yao', 'shao', 'zhan', 'wang1', 'qi2', 'mao', 'yu4', 'di', 'mi', 'bei', 'ming',
             'zang', 'ji', 'fu1', 'cheng', 'dai', 'tan', 'song', 'mao1', 'pang', 'xiong', 'ji1',
             'shu', 'qu', 'xiang', 'zhu1', 'dong', 'du', 'ruan', 'lan', 'min', 'xi1', 'ji2', 'ma1',
             'qiang', 'jia', 'lu2', 'lou', 'wei3', 'jiang2', 'tong', 'yan1', 'guo', 'mei', 'sheng',
             'lin', 'diao', 'tzeng', 'xu1', 'chiu', 'lo1', 'gao', 'xia', 'tzai', 'tian', 'fan1', 'hu']
    info = MyMysql('localhost', 3306, 'root', '123456', 'spider', 'utf8')
    for name in names:
        for i in range(10):
            url = "http://%s.resgain.net/name_list_%d.html" % (name, i)
            html = get_one_page(url)
            datas = parse_with_xpath(html)
            for data in datas:
                sql = 'insert into baijiaxing_two(name, usename) values("%s", "%s")' % (data, name)
                print('*' * 10)
                info.insert_info(sql)
    print('存储成功')


if __name__ == '__main__':
    main()
