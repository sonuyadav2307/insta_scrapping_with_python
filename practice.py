from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import re

driver = webdriver.Chrome(executable_path='/home/Sonu/Documents/Sonu/chromedriver')
driver.maximize_window()
driver.get('https://www.instagram.com/explore/tags/outdoor/?hl=en')
driver.implicitly_wait(10)
def hashtagfinder(hash):
    hashfinder = re.compile(r'#\w+')
    ele = hashfinder.findall(hash)
    return(ele)
def login():
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div/div/div/div[3]/div[1]/a').click()
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
    
    
login()
time.sleep(5)
list1= []
for i in range(1):
    driver.execute_script('window.scrollBy(0,1100)','')
    #driver.execute_script('window.scrollBy(0,document.body.scrollHeight)')
    time.sleep(2)
    source = driver.page_source
    soup = BeautifulSoup(source,'html.parser')
    t = soup.find_all(class_='Nnq7C weEfm')
    t = str(t)
    bake = BeautifulSoup(t,'html.parser')

    for i in bake.find_all('a',href =True):
        list1.append('https://www.instagram.com'+i['href'])
def compare(list2):
    ele = set(list2)
    return ele    
x = compare(list1)
length = len(x)
houragolink = []

for i in x:
    driver.get(i)
    time.sleep(2)
    a = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[3]/div[2]/a/time')
    a = str(a.text)
    p = re.compile(r'SECONDS|MINUTES|HOURS|DAY|MINUTE|HOUR')
    y = p.findall(a)
    # print (y)
    
    if y[0] == 'SECONDS':
        houragolink.append(i)
    elif y[0] == 'MINUTES':
        houragolink.append(i)
    elif y[0] == 'MINUTE':
        houragolink.append(i)   
    else:
        continue 
#print (hourbeforelink)            

time.sleep(1)
hashtaglist = []
linkandurl = {}
for i in houragolink:
    driver.get(i)
    source = driver.page_source
    soup = BeautifulSoup(source,'html.parser')
    a = soup.find_all(class_='C4VMK')#KC1QD
    a = str(a)
    time.sleep(2)
    new = hashtagfinder(a)
    hashtaglist.append(new)
    #print(new)
    time.sleep(2)
    linkandurl[i]=new
# print (linkandurl) 

 
    




    