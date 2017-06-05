#coding = utf-8
from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
url = 'http://www.baidu.com'
driver.get(url)
driver.close()
