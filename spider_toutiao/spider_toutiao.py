import threading
import requests
import pymongo
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


def international_toutiao(a):
    print('线程为%s,接受过来的参数为%s' % (threading.current_thread().name, a))
    client = pymongo.MongoClient(host='localhost', port=27017)

    db = client.toutiao
    collection = db.international_toutiao
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
        print('国际')


def military_toutiao(b):
    print('线程为%s,接受过来的参数为%s' % (threading.current_thread().name, b))
    client = pymongo.MongoClient(host='localhost', port=27017)

    db = client.toutiao
    collection = db.military_toutiao
    for page in range(8):
        url = f'https://www.toutiao.com/search_content/?offset={page * 20}&format=json&keyword=%E5%86%9B%E4%BA%8B&autoload=true&count=20&cur_tab=1&from=search_tab&pd=synthesis'

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
        print('军事')


def sports_toutiao(c):
    print('线程为%s,接受过来的参数为%s' % (threading.current_thread().name, c))
    client = pymongo.MongoClient(host='localhost', port=27017)

    db = client.toutiao
    collection = db.sports_toutiao
    for page in range(8):
        url = f'https://www.toutiao.com/search_content/?offset={page*20}&format=json&keyword=%E4%BD%93%E8%82%B2&autoload=true&count=20&cur_tab=1&from=search_tab&pd=synthesis'

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
        print('体育')


def entertainment_toutiao(d):
    print('线程为%s,接受过来的参数为%s' % (threading.current_thread().name, d))
    client = pymongo.MongoClient(host='localhost', port=27017)

    db = client.toutiao
    collection = db.entertainment_toutiao
    for page in range(8):
        url = f'https://www.toutiao.com/search_content/?offset={page * 20}&format=json&keyword=%E5%A8%B1%E4%B9%90&autoload=true&count=20&cur_tab=1&from=search_tab&pd=synthesis'

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
        print('娱乐')


def car_toutiao(e):
    print('线程为%s,接受过来的参数为%s' % (threading.current_thread().name, e))
    client = pymongo.MongoClient(host='localhost', port=27017)

    db = client.toutiao
    collection = db.car_toutiao
    for page in range(8):
        url = f'https://www.toutiao.com/search_content/?offset={page * 20}&format=json&keyword=%E6%B1%BD%E8%BD%A6&autoload=true&count=20&cur_tab=1&from=search_tab&pd=synthesis'
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
        print('汽车')


def main():
    a = '国际'
    b = '军事'
    c = '体育'
    d = '娱乐'
    e = '汽车'
    t_international = threading.Thread(target=international_toutiao, name='国际', args=(a, ))
    t_military = threading.Thread(target=military_toutiao, name='军事', args=(b, ))
    t_sports = threading.Thread(target=sports_toutiao, name='体育', args=(c, ))
    t_entertainment = threading.Thread(target=entertainment_toutiao, name='娱乐', args=(d, ))
    t_car = threading.Thread(target=car_toutiao, name='汽车', args=(e, ))

    # 启动线程
    t_international.start()
    t_military.start()
    t_sports.start()
    t_entertainment.start()
    t_car.start()

    # 等待主线程结束
    t_international.join()
    t_military.join()
    t_sports.join()
    t_car.join()


if __name__ == '__main__':
    main()