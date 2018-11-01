import time
from io import BytesIO

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lxml import etree
from PIL import Image
from chaojiying import main1
from lxml import etree

# 无头浏览器
# chrome_options = webdriver.ChromeOptions()
# # chrome_options.add_argument('--headless')
# browser = webdriver.Chrome(chrome_options=chrome_options)

# # browser = webdriver.Chrome()
# browser.set_window_size(1400, 1000)
# wait = WebDriverWait(browser, 10)


def get_page_image():

    for i in range(500):
        url = 'http://www.1kkk.com/image3.ashx?t=154080080700%d' % i
        headers = {
            "User-Agent": "Mozilla/4.0 (compatible;MSIE 7.0; Windows NT 5.1; 360SE)"
        }
        response = requests.get(url, headers)
        if response.status_code == 200:
            image = response.content
        with open('./image/%s' % ("%d.png" % i), 'wb')as f:
            f.write(image)
        print('************')


def main():
    # get_page_image()
    copy_image()


def copy_image():
    for a in range(500):
        screenshot = Image.open("./image/%d.png" % a)
        screenshot.crop()
        for i in range(4):
            crop_img = screenshot.crop((76*i, 0, 76*(i+1), 76))
            file_name = 'image%d_%d.png' % (a, i)
            crop_img.save('./image2/'+file_name)


if __name__ == '__main__':
    main()
