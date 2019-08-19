#-*- coding: utf-8 -*-
'''
---------------

Description of this file

:author: Luopeng
:date created: 2019-08-09
:python version: 3.6

---------------
'''
# 时间：2019-4-8
# 内容：爬取今日头条的热点栏目

import requests
import json
import time


_url = "https://www.toutiao.com/api/pc/feed/?category=news_hot&utm_source=toutiao&widen=1&max_behot_time=1554765316&max_behot_time_tmp=1554765316&tadrequire=true&as=A1250C3AEBADDD2&cp=5CABCDED7D427E1&_signature=Fz.gqgAAS5i9EKAq5BB9EBc.4L"
url1 = "https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset=0&format=json&keyword=%E5%9B%BE%E7%89%87&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1565331855011"
_headers = {
    'cookie': 'tt_webid=6677522179426485774; WEATHER_CITY=%E5%8C%97%E4%BA%AC; UM_distinctid=169fd3c82d31d-03d38d9bfe605d-77103a49-100200-169fd3c82d41d5; tt_webid=6677522179426485774; csrftoken=29a9338e5f4bc1c2fd7fe29e5caf39c5; sso_uid_tt=d28e7e0d21e1ff621101e7f4d06c25de; toutiao_sso_user=56b1c51186f1dca408808ec2a7153851; login_flag=6413115c5ffc0dc3955803ad1d951ff5; sessionid=cd2c4291a9d47c540ec712e3b298b401; uid_tt=f418766df0e6eb1a6da8f965c6da76a8; sid_tt=cd2c4291a9d47c540ec712e3b298b401; sid_guard="cd2c4291a9d47c540ec712e3b298b401|1554731811|15552000|Sat\054 05-Oct-2019 13:56:51 GMT"; __tasessionId=gvgwyytsx1554767065092; CNZZDATA1259612802=152351107-1554731013-https%253A%252F%252Fwww.baidu.com%252F%7C1554762386',

    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3642.0 Safari/537.36'

}


# 获取json文件
def get_info(url, headers):
    response = requests.get(url, headers=headers)
    print(response)
    return response


# 将有用的信息保存到文件中
def save(response):
    file = open("toutiao1.json", "a", encoding="utf-8")
    # 有用信息包含在response.json()["data"]中
    json.dump(response.json()["data"],file,ensure_ascii=False)


# 主函数，调用获取和保存的函数成果
def run(url, headers):
    for i in range(1):
        response = get_info(url, headers)
        save(response)
        time.sleep(3)
    return


if __name__ == '__main__':
    run(_url, _headers)


