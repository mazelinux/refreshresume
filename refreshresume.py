#coding = utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import threading
import random
import logging
import time

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

def refreshresume_51job():
    driver = webdriver.Firefox()
    url = 'http://www.51job.com'
    driver.get(url)
    sleep(1)
    driver.find_element_by_xpath("//a[contains(text(),'登录')]").click()
    sleep(1)
    driver.find_element_by_xpath("//input[@id='loginname' and @type='text']").send_keys(uname)
    sleep(1)
    driver.find_element_by_xpath("//input[@id='password' and @name='password']").send_keys(psword)
    sleep(1)
    print(driver.find_element_by_xpath("//button[@id='login_btn']").click())
    driver.find_element_by_xpath("//button[@id='login_btn']").click()
    sleep(5)
    driver.get('http://m.51job.com/my/my51job.php')
    sleep(5)
    driver.get('http://m.51job.com/resume/myresume.php')
    sleep(5)
    print(driver.find_element_by_xpath("//li[@class='l1 bb']").click())
    sleep(5)
    driver.close()
    
def do_refreshresume_firefox():
    try:
        refreshresume_liepin()
        refreshresume_zhilian()
        refreshresume_51job()
        sleep(random.randint(200,400))
    except Exception as e:
        logging.exception(e)

if __name__ == "__main__":
    i = 0
    while True:
        print("resume start")
        print("%d次刷新,刷新时间是"%(i),end='')
        i = i+1
        print(time.strftime("%Y-%m-%d  %H:%M:%S", time.localtime() ))
        do_refreshresume_firefox()
        print("resume finish")

