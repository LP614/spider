from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote
from lxml import etree


chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)

browser.set_window_size(1400, 700)
wait = WebDriverWait(browser, 10)
KEYWORD = '笔记本电脑'


def get_page(page):
    url = 'https://search.jd.com/Search?keyword=%s&enc=utf-8' % quote(KEYWORD)
    browser.get(url)
    if page > 1 :
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        input = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'J_bottomPage input.input-text')))
        input.clear()
        input.send_keys(page)

        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_bottomPage a.btn.btn-def')))
        submit

def main():
    get_page()


if __name__ == '__main__':
    main()