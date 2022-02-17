from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as Soup
import time
from selenium.webdriver.common.keys import Keys
option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')


browser = webdriver.Chrome(chrome_options=option)
url = 'https://www.instagram.com/p/CE_bR-osw4M/'
browser.get(url)

soup=Soup(browser.page_source,"lxml")
soup.find_all(class_="KL4Bh")[0].img.get('src')


time.sleep(10)
#browser.close()

#video

#url='https://www.instagram.com/p/CFwyL6s9Gn/'
#browser.get(url)

#soup=Soup(browser.page_source,"lxml")
#soup.find_all(class_="_swCQW")[0].video.get('src')