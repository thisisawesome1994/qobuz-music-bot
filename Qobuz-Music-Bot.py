from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.options import Options
from random import randint
from time import sleep
import os
import time
import random

proxy = random.choice(open('proxies.txt').readlines())
useragent = random.choice(open('useragents.txt').readlines())
url = random.choice(open('links.txt').readlines())
username = open('username.txt', 'r', encoding='utf-8').readlines()
password = open('password.txt', 'r', encoding='utf-8').readlines()


opts1 = Options()
opts1.add_argument('--user-agent=%s'% useragent)
#opts1.add_argument('--mute-audio')
opts1.add_argument('--incognito')
opts1.add_argument('--proxy-server=%s'% proxy)
#opts1.add_argument('--headless')
opts1.add_argument('--start-maximized')
browser1 = webdriver.Chrome(options=opts1)
browser1.execute_script("window.location.replace(arguments[0])", url)
time.sleep(10)
login = browser1.find_element_by_xpath(""" //*[@id="root"]/div/div/div[3]/div/div[2]/div/div[3]/form/div[1]/div/fieldset/input """).send_keys(username)
time.sleep(2)
password = browser1.find_element_by_xpath(""" //*[@id="root"]/div/div/div[3]/div/div[2]/div/div[3]/form/div[2]/div/fieldset/input """).send_keys(password)
time.sleep(2)
submit = browser1.find_element_by_xpath(""" //*[@id="root"]/div/div/div[3]/div/div[2]/div/div[3]/form/p[1]/button """)
submit.click()
time.sleep(15)
play_button = browser1.find_element_by_xpath(""" //*[@id="root"]/div/div/div[3]/div/div[2]/section/div/div/div/div/div/ul/li[2]/div/span[1]/a/span """)
time.sleep(2)
play_button.click()
time.sleep(randint(180,3200))
os.startfile("launch.exe")
browser1.quit()
# script by thisisawesome1994