#coding = utf-8
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
#模拟按键
from selenium.webdriver.common.action_chains import ActionChains
#模拟鼠标
import win32gui

def login():	
#url = 'http://pub.alimama.com/promo/search/index.htm'
#    url = 'https://www.alimama.com/index.htm'
    url = 'https://login.taobao.com/member/login.jhtml?style=mini&newMini2=true&css_style=alimama&from=alimama&redirectURL=http%3A%2F%2Fwww.alimama.com&full_redirect=true&disableQuickLogin=true'
    driver.get(url)
    sleep(1)
#    driver.find_element_by_xpath("//span[contains(text(),'亲，请登录')]").click()
#   driver.find_element_by_xpath("//div[@class = 'login-switch']").click()
    driver.find_element_by_link_text("密码登录").click()
    driver.find_element_by_id('TPL_username_1').send_keys(uname)
    sleep(3)
    driver.find_element_by_id('TPL_password_1').send_keys(psword)
    sleep(3)
    driver.find_element_by_id('TPL_password_1').send_keys(Keys.ENTER)
    sleep(3)
#driver.find_element_by_id('J_SubmintStatic').click()
    try:
        slider = driver.find_element_by_id('nc_1_n1z')
        print("slider appear")
        print(slider)
#        ActionChains(driver).click_and_hold(slider).move_by_offset(1000,300).release().perform()
        actions = ActionChains(driver)
        actions.click_and_hold(slider)
        actions.move_by_offset(1000,220)
        actions.release()
        actions.perform()
        print("slider done")
        print(win32gui.GetCursorPos())
    except:
        print("no slider")
	
def jump2lianmeng_search_good():
    url = 'https://pub.alimama.com'
    driver.get(url)
    sleep(3)
    driver.find_element_by_xpath("/html/body//div//div//div//div//div//div/input[@id='q']").send_keys(goods)
    driver.find_element_by_xpath("/html/body//div//div//div//div//div//div/input[@id='q']").send_keys(Keys.ENTER)
#    input_word = driver.find_element_by_class('search-inp input').send_keys(goods)
if __name__ == "__main__":
    uname = ""
    psword = ""
    goods = "衣服"
    driver = webdriver.Firefox()
    login()
    jump2lianmeng_search_good()
