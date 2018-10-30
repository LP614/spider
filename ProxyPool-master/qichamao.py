import json
import requests
from lxml import etree
from agent_helper import get_random_agent
from dailichi import get_proxy

agent = get_random_agent()


class Qichamao(object):
    def __init__(self):
        self.url = 'https://www.qichamao.com/cert-wall'
        self.headers = {
            'Referer': 'https://qichamao.com/',
            'User-Agent': agent,
            'Host': 'www.qichamao.com'
        }
        self.session = requests.Session()

    def parse_page(self, html):
        selector = etree.HTML(html)
        company_items = selector.xpath('//div[@class="firmwall_list_box"]')
        company_list = []
        for company_item in company_items:
            company_dict = {}
            companyname = company_item.xpath('.//*[@class="firmwall_list_tit toe"]/a/text()')
            company_dict['company_name'] = companyname
            company_list.append(company_dict)
        return company_list

    def get_page(self):
        response = self.session.get(self.url, headers=self.headers)
        if response.status_code == 200:
            return response.content.decode('utf-8')
        else:
            return None

    def post_page(self, page, pagesize,proxies):
        data = {'page':page, 'pagesize':pagesize}
        response = self.session.post(self.url, headers=self.headers, data=data, proxies=proxies)
        if response.status_code == 200:
            return response.content.decode('utf-8')
        else:
            return None

    def parse_json(self, json_text):
        result_json = json.loads(json_text)
        data_list = result_json['datalist']
        for data in data_list:
            print(data['CompanyName'])


def main():
    qichamao = Qichamao()
    html = qichamao.get_page()
    results = qichamao.parse_page(html)
    print('page1')
    for item in results:
        print(item['item_name'])
    for i in range(100):
        proxy = get_proxy()
        proxies = {
            'http': 'http://' + proxy,
            'https': 'https://' + proxy,
        }
        print('page%d' % (i+2))
        print('*'*20)
        json_text = qichamao.post_page(i+2, 9, proxies)
        qichamao.parse_json(json_text)


if __name__ == '__main__':
    main()
