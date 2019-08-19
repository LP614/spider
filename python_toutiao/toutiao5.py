#-*- coding: utf-8 -*-
'''
---------------

Description of this file

:author: Luopeng
:date created: 2019-08-16
:python version: 3.6

---------------
'''
import pymongo
import requests
import json

import time
import hashlib
import os
import datetime

start_url = 'https://www.toutiao.com/api/pc/feed/?category=news_hot&utm_source=toutiao&widen=1&max_behot_time='
url = 'https://www.toutiao.com'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
cookies = {'tt_webid': '6722356446824613389'}  # 此处cookies可从浏览器中查找，为了避免被头条禁止爬虫

max_behot_time = '0'  # 链接参数
title = []  # 存储新闻标题
source_url = []  # 存储新闻的链接
s_url = []  # 存储新闻的完整链接
source = []  # 存储发布新闻的公众号
media_url = {}  # 存储公众号的完整链接


def get_as_cp():  # 该函数主要是为了获取as和cp参数，程序参考今日头条中的加密js文件：home_4abea46.js
    zz = {}
    now = round(time.time())
    print(now)  # 获取当前计算机时间
    e = hex(int(now)).upper()[2:]  # hex()转换一个整数对象为16进制的字符串表示
    print('e:', e)
    a = hashlib.md5()  # hashlib.md5().hexdigest()创建hash对象并返回16进制结果
    print('a:', a)
    a.update(str(int(now)).encode('utf-8'))
    i = a.hexdigest().upper()
    print('i:', i)
    if len(e) != 8:
        zz = {'as': '479BB4B7254C150',
              'cp': '7E0AC8874BB0985'}
        return zz

    n = i[:5]
    a = i[-5:]
    r = ''
    s = ''
    for i in range(5):
        s = s + n[i] + e[i]
    for j in range(5):
        r = r + e[j + 3] + a[j]
    zz = {
        'as': 'A1' + s + e[-3:],
        'cp': e[0:3] + r + 'E1'
    }
    print('zz:', zz)
    return zz


def getdata(url, headers, cookies):  # 解析网页函数
    r = requests.get(url, headers=headers, cookies=cookies)
    print(url)
    data = json.loads(r.text)
    return data


def main(max_behot_time, title, source_url, s_url, source, media_url):  # 主函数

    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client.toutiao
    collection = db.toutiao
    for i in range(10):  # 此处的数字类似于你刷新新闻的次数，正常情况下刷新一次会出现10条新闻，但夜存在少于10条的情况；所以最后的结果并不一定是10的倍数
        time.sleep(2)
        data_list = []
        ascp = get_as_cp()  # 获取as和cp参数的函数
        demo = getdata(
            start_url + max_behot_time + '&max_behot_time_tmp=' + max_behot_time + '&tadrequire=true&as=' + ascp[
                'as'] + '&cp=' + ascp['cp'], headers, cookies)
        infos = demo['data']
        for info in infos:
            data = {'abstract': info['abstract'] if info.get('abstract') else '',
                    'chinese_tag': info['chinese_tag'] if info.get('chinese_tag') else '',
                    'title': info['title'] if info.get('title') else '',
                    'source': info['source'] if info.get('source') else '',
                    'middle_image': info['middle_image'] if info.get('middle_image') else ''}
            data_list.append(data)
    #将数据保存为json文件
    str = json.dumps(data_list, ensure_ascii=False)
    with open('textone.json', 'w', encoding='utf-8') as f:
        f.write(str)
    #存入mongodb数据库
    collection.insert_many(data_list)


if __name__ == '__main__':
    main(max_behot_time, title, source_url, s_url, source, media_url)
