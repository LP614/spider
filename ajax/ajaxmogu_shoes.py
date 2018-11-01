
import requests
import json
from my_mysql import MyMysql



def get_one_page(url):
    headers = {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        text = response.content.decode('utf-8')
        return text
    return None


def get_real_content(html):
    if html and len(html) > 128:
        i = html.index('(')
        html1 = html[i+1:]
        html2 = html1.replace(');', '')
        return html2
    return None


def main():
    info = MyMysql('localhost', 3306, 'root', '123456', 'spider', 'utf8')
    flag = False
    while True:
        try:
            with open('page_number.txt', 'r', encoding='utf8') as f:
                page = int(f.read())
            break
        except Exception as e:
            print(e)
            with open('page_number.txt', 'w', encoding='utf8') as f:
                page_init = '1'
                f.write(page_init)

    while not flag:
        url = "https://list.mogujie.com/search?callback=jQuery211021795453828997524_1540391254575&_version=8193&ratio=3%3A4&cKey=15&page="+str(page)+"&sort=pop&ad=0&fcid=51267&action=shoes&acm=3.mce.1_10_1her0.109753.0.9XpX1r7paCDfw.pos_1-m_406106-sd_119-mf_15261_1047900-idx_0-mfs_76-dm1_5000&ptp=1._mf1_1239_15261.0.0.mN4NXuTW&_=1540391254578"
        try:
            html = get_one_page(url)
        except Exception as e:
            with open('page_number.txt', 'w', encoding='utf8') as f:
                f.write(str(page))
            print(e)
            break
        html_content = get_real_content(html)
        # print(html_content)
        result = json.loads(html_content)
        goods_info = result['result']['wall']['docs']
        print(goods_info)
        flag = result['result']['wall']['isEnd']
        for i in goods_info:
            sql = 'insert into ajaxmogu_shoes(tradeItemId, img, clientUrl, link, acm, title, cparam, orgPrice, sale, cfav, price, similarityUrl) values("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")' % (i['tradeItemId'], i['img'], i['clientUrl'], i['link'], i['acm'], i['title'], i.get('cparam') if i.get('cparam') else '', i['orgPrice'], i['sale'], i['cfav'], i['price'], i['similarityUrl'])
            info.insert_info(sql)
            print(flag, page)
        if flag:
            with open('page_number.txt', 'w', encoding='utf8') as f:
                f.write(str(page)+'spider over')
        page += 1


if __name__ == '__main__':
    main()