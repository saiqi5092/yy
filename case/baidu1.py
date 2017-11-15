# coding=utf-8
from selenium import webdriver
import time

# 配置文件地址
profile_directory = r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\z9ej8poa.default'
# 加载配置
profile = webdriver.FirefoxProfile(profile_directory)
# 启动浏览器配置

driver = webdriver.Firefox(profile)
url1 = "https://www.baidu.com"
driver.get(url1)
element = driver.find_element_by_id("kw")  # 定位元素
print element
element.send_keys("yoyo")  # 发送文本
element.send_keys(u"中文")  # 发送文本
driver.find_element_by_id("su").click()
