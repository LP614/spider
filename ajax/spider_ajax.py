import requests
import pymysql
import json




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
        html2 = html1.replace(');','')
        return html2
    return None


def main():
    url = "https://list.mogujie.com/search?callback=jQuery2110023070051465743147_1540348080741&_version=8193&ratio=3%3A4&cKey=43&sort=pop&page=1&q=%25E5%258D%25AB%25E8%25A1%25A3&minPrice=&maxPrice=&ppath=&cpc_offset=&acm=3.mce.1_4_11k.39084.77211.pC6Ulr7mfwYBQ.p_12_hotSearchKeywordRec-mid_39084-sd_115-mdt_sketch-dit_29-lc_201&from=searchplacehold&ptp=1._mf1_1239_15261.0.0.XY14K3X6&_=1540348080742"
    html = get_one_page(url)
    print(html)
    html_content = get_real_content(html)
    print(html_content)
    result = json.loads(html_content)
    goods_info = result['result']['wall']['docs']
    # print(result['tradeItemId'])
    db = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='spider', charset='utf8')
    cursor = db.cursor()
    for i in goods_info:
        sql = 'insert into ajax(tradeItemId, img, itemType, link, itemMarks, acm, title, type, orgPrice, cfav, price, similarityUrl) values("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", )' % (
        i['tradeItemId'], i['img'], i['itemType'], i['link'], i['itemMarks'], i['acm'], i['title'], i['type'],
        i['orgPrice'], i['cfav'], i['price'], i['similarityUrl'])
        cursor.execute(sql)
        db.commit()



if __name__ == '__main__':
    main()