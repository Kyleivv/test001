from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver =webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.maximize_window() #窗口化放大网站
