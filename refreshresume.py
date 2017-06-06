#coding = utf-8
from selenium import webdriver
from time import sleep
import threading
import random

def refreshresume_liepin():
    driver = webdriver.Firefox()
    url = 'https://www.liepin.com'
    driver.get(url)
    sleep(1)
    #driver.find_element_by_xpath("//标签名[@属性='属性值' and @属性='属性值']")
    driver.find_element_by_xpath("//a[contains(text(),'马上登录')]").click()
    sleep(1)
    username = driver.find_element_by_xpath("//input[@type='text' and @name='user_login']").send_keys('406732060@qq.com')
    sleep(1)
    password = driver.find_element_by_xpath("//input[@type='password']").send_keys('xxxxx')
    sleep(1)
    driver.find_element_by_xpath("//input[@value='登 录' and @type='submit']").click()
    sleep(1)
    driver.find_element_by_xpath("//span[contains(text(),'刷新简历')]").click()
    sleep(5)
    driver.close()

def refreshresume_zhilian():
    driver = webdriver.Firefox()
    url = 'https://www.zhaopin.com'
    driver.get(url)
    sleep(1)
    driver.find_element_by_xpath("//input[@id='loginname' and @name='loginname']").send_keys('406732060@qq.com')
    sleep(1)
    driver.find_element_by_xpath("//input[@id='password' and @name='Password']").send_keys('xxxxxxxxxxxxxx')
    sleep(1)
    driver.find_element_by_xpath("//button[@type='submit']").click()
    sleep(1)
#driver.find_element_by_xpath("//span[@class='fr.popup_close']").click()
#driver.find_element_by_class_name('fr popup_close').click()
#driver.find_element_by_xpath("//a[@class='myLinkA linkRefresh']").click()
    driver.get(url)
    sleep(5)
    driver.find_element_by_xpath("//a[@id='refresh']").click()
    sleep(5)
    driver.close()

def do_refreshresume():
    refreshresume_liepin()
    refreshresume_zhilian()
    sleep(random.randint(300,900))
    timer.start()

if __name__ == "__main__":
    timer = threading.Timer(1,do_refreshresume)
    print("start timer")
    timer.start()
