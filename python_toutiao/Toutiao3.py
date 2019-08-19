#-*- coding: utf-8 -*-
'''
---------------

Description of this file

:author: Luopeng
:date created: 2019-08-09
:python version: 3.6

---------------
'''
import json

import pymysql
import requests

# end_page = int(input('请输入结束页面：'))
# keyword = input('请输入查找关键字：')
end_page = 3
keyword = "图片"


def get_url():
    for page in range(end_page):
        offset = (page - 1) * 20
        url = 'https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset=20&format=json&keyword=%E5%9B%BE%E7%89%87&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1565335780343'
        params = {
            'offset': offset,
            'format': 'json',
            'keyword': keyword,
            'autoload': 'true',
            'count': '20',
            'cur_tab': '1',
            'from': 'search_tab'
        }
        # param = {
        #     'aid': '24',
        #     'app_name': 'web_search',
        #     'offset': 20,
        #     'format': 'json',
        #     'keyword': '图片',
        #     'autoload': 'true',
        #     'count': 20,
        #     'en_qc': 1,
        #     'cur_tab': 1,
        #     'from': 'search_tab',
        #     'pd': 'synthesis',
        #     'timestamp': 1565335780343,
        # }
        headers = {
            'referer': 'https://www.toutiao.com/search/?keyword=%E5%9B%BE%E7%89%87',
            'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
            'x-requested-with': 'XMLHttpRequest'
        }
        # headers = {
        #     'Referer': url,
        #     'Host':'www.u17.com',
        #     'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
        #     'Accept': 'application/json, text/plain, */*',
        #     'Accept-Encoding': 'gzip, deflate, sdch',
        #     'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2,mt;q=0.2',
        #     'Connection': 'keep-alive',
        #     'X-Requested-With': 'XMLHttpRequest',
        #     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # }
        try:
            session = requests.Session()
            response = session.get(url, headers=headers)
            if response.status_code == 200:
                text = response.content.decode('utf-8')
                print(text, "++++++++")
                return text
            # toutiao_json = requests.get(url, params=params, headers=headers).text
            # print(toutiao_json, "++++")
            # return toutiao_json
        except:
            return None


def get_toutiao(toutiao_json):
    json_toutiao = json.loads(toutiao_json)
    print(json_toutiao, "+++")
    data_list = json_toutiao['data']
    items = []
    for data in data_list:
        if data.get('title'):
            title = data.get('title')
            images = data.get('image_list')
            url_list = []
            for image in images:
                url = 'https:' + image['url']
                url_list.append(url)
            dict1 = {
                'title': title,
                'image': url_list
            }
            items.append(dict1)
    return items


def save_content(items):
    filename = keyword + '.txt'
    for item in items:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(json.dumps(item, ensure_ascii=False))


def main():
    toutiao_json = get_url()
    items = get_toutiao(toutiao_json)
    save_content(items)


if __name__ == '__main__':
    main()