#coding = utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import threading
import random
import logging

def refreshresume_liepin():
    driver = webdriver.Firefox()
    url = 'https://www.liepin.com'
#   try:
#driver.implicitly_wait(10)
    driver.get(url)
#    WebDriverWait(driver,10).until(lambda x: x.find_element_by_xpath("//a[contains(text(),'马上登录')]").click())
    #driver.find_element_by_xpath("//标签名[@属性='属性值' and @属性='属性值']")
    driver.find_element_by_xpath("//a[contains(text(),'马上登录')]").click()
    sleep(5)

#    WebDriverWait(driver,10).until(lambda x: x.find_element_by_xpath("//input[@type='text' and @name='user_login']").send_keys(uname))
    print(driver.find_element_by_xpath("//input[@type='text' and @name='user_login']").send_keys(uname))
    sleep(5)
    print(driver.find_element_by_xpath("//input[@type='password']").send_keys(psword))
    print(driver.find_element_by_xpath("//input[@value='登 录' and @type='submit']").click())
    sleep(5)

#WebDriverWait(driver,10).until(lambda x: x.find_element_by_xpath("//span[contains(text(),'刷新简历')]").click()) 
    print(driver.find_element_by_xpath("//span[contains(text(),'刷新简历')]").click())
    sleep(5)
#   finally:
    driver.close()

def refreshresume_zhilian():
    driver = webdriver.Firefox()
    url = 'https://www.zhaopin.com'
#    try:
    driver.get(url)
    sleep(1)
    driver.find_element_by_xpath("//input[@id='loginname' and @name='loginname']").send_keys(uname)
    sleep(1)
    driver.find_element_by_xpath("//input[@id='password' and @name='Password']").send_keys(psword)
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
#   finally:
    driver.close()

def do_refreshresume_firefox():
    try:
        refreshresume_liepin()
        refreshresume_zhilian()
        sleep(random.randint(200,400))
    except Exception as e:
        logging.exception(e)

if __name__ == "__main__":
    uname = ""
    psword = ""
    while True:
        print("resume start")
        do_refreshresume_firefox()
        print("resume finish")

