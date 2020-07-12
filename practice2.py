from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import re
list1= ['https://www.instagram.com/p/CCT5MUKneNF/','https://www.instagram.com/p/CCU76EPq30X/']
driver = webdriver.Chrome(executable_path='/home/Sonu/Documents/Sonu/chromedriver')
driver.maximize_window()
driver.get('https://www.instagram.com/p/CCT5MUKneNF/')
def login():
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div/div/div/div[3]/div[1]/a').click()
    time.sleep(2)
    ele = driver.find_element_by_name('username')
    #print(ele.is_displayed())
    ele.send_keys('yadav.sonu2307@gmail.com')
    pwd = driver.find_element_by_name('password')
    pwd.send_keys('Sonu@2307')
    login = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]').click()
    time.sleep(2)
    driver.back()
    time.sleep(2)
    driver.back()
    time.sleep(2)
time.sleep(2)    
login ()    
for i in list1:
    driver.get(i)
    time.sleep(2)
    a = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/article/div[2]/div[2]/a/time')
    a = str(a.text)
    x = re.compile(r'SECONDS|MINUTES|HOURS|DAY')
    y = x.findall(a)
    hourbeforelink = []
    print (y)
    if y[0] == 'SECONDS':
        hourbeforelink.append(i)
    elif y[0] == 'MINUTES':

        print (i) 
    else:
        continue     
