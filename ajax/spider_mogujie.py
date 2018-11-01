import requests
import pymysql
import json


# 取页面HTML
def get_one_page():
    url = 'https://list.mogujie.com/search?callback=jQuery21104432147899441732_1540347837433&_version=8193&ratio=3%3A4&cKey=15&page=1&sort=pop&ad=0&fcid=50206&action=trousers&acm=3.mce.1_10_1hepw.109731.0.ubj8Qr7mesgMd.pos_1-m_406086-sd_119-mf_15261_1047900-idx_0-mfs_4-dm1_5000&ptp=1._mf1_1239_15261.0.0.wdmwVEI3&_=1540347837434'
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
        html1 = html.split('(')[1:][0]
        html1 = html1.replace(');', '')
        return html1
    return None


def main():
    html = get_one_page()
    html_content = get_real_content(html)
    print(html_content)
    goods_info = json.loads(html_content)
    result = goods_info['result']['wall']['docs']
    # print(result['tradeItemId'])
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='spider', charset='utf8')
    cursor = db.cursor()
    for i in result:
		sql = 'insert into ajax(tradeItemId, img, itemType, link, itemMarks, acm, title, type, orgPrice, cfav, price, similarityUrl) values("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", )' % (i['tradeItemId'], i['img'], i['itemType'],i['link'], i['itemMarks'], i['acm'],i['title'], i['type'], i['orgPrice'],i['cfav'], i['price'], i['similarityUrl'])
		cursor.execute(sql)
		db.commit()


if __name__ == '__main__':
    main()
