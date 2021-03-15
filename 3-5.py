import time  # python 内置的模 直接引用即可
from selenium import webdriver   # 1-安装selenium模块  cmd -->pip install selenium  2-下载ChromeDriver 加压放再Chrome的安装路径中

ChromeDriver = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
# 声明一个浏览器对象  指定使用chromedriver.exe路径
browser = webdriver.Chrome(executable_path=ChromeDriver)

# 打开Chrome 打开指定的网址
browser.get("https://www.baidu.com")

# 通过id定位到input框
input0 = browser.find_element_by_id("kw")

# 在输入框输入python
input0.send_keys("python")
time.sleep(2)

# 通过id定位到百度一下按钮
button = browser.find_element_by_id("su")
# 点击百度按钮
button.click()
# # 打印url
# print(browser.current_url)

# # 打印Cookies
# print(browser.get_cookie())

# # 打印网页源代码
# print(browser.page_source)
time.sleep(10)

# 关闭浏览器
browser.close()
