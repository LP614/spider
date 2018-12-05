import requests
import pymongo
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


def main():
    client = pymongo.MongoClient(host='localhost', port=27017)

    db = client.toutiao
    collection = db.guoji_toutiao
    for page in range(9):
        url = f'https://www.toutiao.com/search_content/?offset={page * 20}&format=json&keyword=%E5%9B%BD%E9%99%85&autoload=true&count=20&cur_tab=1&from=search_tab&pd=synthesis'

        html = get_one_page(url)
        # print(html)
        json_result = json.loads(html)
        print(json_result)
        info_list = json_result['data']
        print(info_list)
        data = []
        for comic in info_list:
            info = {'user_id': comic['user_id'] if comic.get('user_id') else '',
                    'datetime': comic['datetime'] if comic.get('datetime') else '',
                    'title': comic['title'] if comic.get('title') else '',
                    'source': comic['source'] if comic.get('source') else '',
                    'large_image_url': comic['large_image_url'] if comic.get('large_image_url') else '',
                    'comments_count': comic['comments_count'] if comic.get('comments_count') else ''}
            data.append(info)

        collection.insert_many(data)
        print('****')


if __name__ == '__main__':
    main()