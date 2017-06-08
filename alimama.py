#coding = utf-8
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

def login():	
    driver = webdriver.Firefox()
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
    driver.find_element_by_id('TPL_password_1').send_keys(Keys.ENTER)
    sleep(3)
#driver.find_element_by_id('J_SubmintStatic').click()
	
if __name__ == "__main__":
    uname = "18818204314"
    psword = "406732060chen"
    login()
