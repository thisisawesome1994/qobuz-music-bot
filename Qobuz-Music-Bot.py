from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.options import Options
import time
views = int=1000000
view_time = float=2000
proxy = "p.webshare.io:19999"

opts1 = Options()
opts1.add_argument('--user-agent=[Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36]')
#opts1.add_argument('--mute-audio')
opts1.add_argument('--incognito')
opts1.add_argument('--proxy-server=%s'% proxy)
#opts1.add_argument('--headless')
opts1.add_argument('--start-maximized')

browser1 = webdriver.Chrome(options=opts1)

# put video link in ''
for i in range(views):
    browser1.get('qobuz album link')
 #   browser1.switch_to.frame("form-horizontal")
 #   browser1.find_element_by_id("login")
 #   browser1.find_element_by_id("password").send_keys("test")
 #   browser1.switch_to.default_content()
    login = browser1.find_element_by_xpath(""" //*[@id="root"]/div/div/div[3]/div/div[2]/div/div[3]/form/div[1]/div/fieldset/input """)
    login.click()
    login = browser1.find_element_by_xpath(""" //*[@id="root"]/div/div/div[3]/div/div[2]/div/div[3]/form/div[1]/div/fieldset/input """).send_keys("username")
    password = browser1.find_element_by_xpath(""" //*[@id="root"]/div/div/div[3]/div/div[2]/div/div[3]/form/div[2]/div/fieldset/input """)
    password.click()
    password = browser1.find_element_by_xpath(""" //*[@id="root"]/div/div/div[3]/div/div[2]/div/div[3]/form/div[2]/div/fieldset/input """).send_keys("password*")
    submit = browser1.find_element_by_xpath(""" //*[@id="root"]/div/div/div[3]/div/div[2]/div/div[3]/form/p[1]/button """)
    submit.click()
#    play_button = browser1.find_element_by_class_name('pct pct-play item-button')
    play_button.click()
    time.sleep(view_time)

browser1.close()


# script by thisisawesome1994