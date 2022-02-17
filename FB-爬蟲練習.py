from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as Soup
import time
from selenium.webdriver.common.keys import Keys

username="a0937357166@gmail.com"
password="a0975008815"
url = 'https://www.google.com/webhp?source=android-home'
spec_url = 'https://www.facebook.com/profile.php?id=100005119578928'
login_url = 'https://zh-tw.facebook.com'

option = webdriver.ChromeOptions()
prefs = {'profile.default_content_setting_values':{'notifications': 2}}
option.add_experimental_option('prefs', prefs)
option.add_argument('disable-infobars')

browser = webdriver.Chrome(chrome_options=option)
browser.maximize_window()




browser.get(login_url)

elem = browser.find_element_by_id("email")
elem.send_keys(username)

elem = browser.find_element_by_id("pass")
elem.send_keys(password)   
elem.send_keys(Keys.ENTER)
time.sleep(1)

browser.get(spec_url)
time.sleep(3)
soup=Soup(browser.page_source,"lxml")
print(soup.find_all('span',class_="d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 d3f4x2em iv3no6db jq4qci2q a3bd9o3v b1v8xokw oo9gr5id")[0].text)


time.sleep(3)
browser.close()


















                      #FB爬蟲練習















