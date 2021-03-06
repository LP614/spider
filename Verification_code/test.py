import time
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lxml import etree
from PIL import Image
from chaojiying import main1

# 无头浏览器
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)

# browser = webdriver.Chrome()
browser.set_window_size(1400, 1000)
wait = WebDriverWait(browser, 10)


def get_page():
    # 进入网页面
    url = 'http://bm.e21cn.com/log/reg.aspx'
    browser.get(url)
    html = browser.page_source
    return html


# 取浏览器窗口全图
def get_big_img():
    # 向下滑动300距离
    browser.execute_script('window.scrollTo(0,100)')
    # 截取浏览器窗口全图
    screenshot = browser.get_screenshot_as_png()
    # 以字节流的形式打开图片
    screenshot = Image.open(BytesIO(screenshot))
    screenshot.save("luo.png")
    return screenshot


# 取验证码坐标位置（左上角和右下角）
def get_position():
    # 找到验证码图片的位置，并获取验证码图片
    img = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#imgCheckCode')))
    loc = img.location
    size = img.size
    print(size)
    print(loc)
    # 图片的坐标
    x3 = 1774 / 887
    y3 = 1120 / 661
    x1 = loc['x'] * x3
    y1 = loc['y'] * y3
    x2 = x1 + size['width'] * x3
    y2 = y1 + size['height'] * y3
    print(x1, y1, x2, y2)
    return (x1, y1, x2, y2)


def parse_html(html):
    # etree_html = etree.HTML(html)
    # 获取带有验证码的浏览器窗口全图
    screenshot = get_big_img()
    # 获取验证码图片的坐标
    x1, y1, x2, y2 = get_position()
    # 按坐标裁剪图片并保存
    crop_img = screenshot.crop((x1, y1, x2, y2))
    file_name = 'crop.png'
    crop_img.save(file_name)
    # 将图片中的字符转换成字符串
    captha_str = main1(file_name)
    print(captha_str)
    # 编辑输入项
    username = 'luopeng'
    password = '123456'
    tel = '18223991007'
    # 获取需要输入input的位置
    input_username = wait.until(EC.presence_of_element_located
                                ((By.CSS_SELECTOR, 'input#username')))
    input_password1 = wait.until(EC.presence_of_element_located
                                 ((By.CSS_SELECTOR, 'input#pwd')))
    input_password2 = wait.until(EC.presence_of_element_located
                                 ((By.CSS_SELECTOR, 'input#pwd_Q')))
    input_tel = wait.until(EC.presence_of_element_located
                           ((By.CSS_SELECTOR, 'input#tel')))
    input_check = wait.until(EC.presence_of_element_located
                             ((By.CSS_SELECTOR, 'input#CheckCode')))
    sublime = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#btn_login')))
    # 向各个input位置填写值
    input_username.send_keys(username)
    input_password1.send_keys(password)
    input_password2.send_keys(password)
    input_tel.send_keys(tel)
    input_check.send_keys(captha_str)
    time.sleep(2)
    sublime.click()


def main():
    html = get_page()
    parse_html(html)


if __name__ == '__main__':
    main()
