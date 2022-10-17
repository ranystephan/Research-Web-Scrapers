from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.options import Options
import random as rd

PATH=r"" #input your webdriver path here
options = Options()
options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
driver = webdriver.Chrome(options = options, executable_path = PATH)

driver.get("https://www.instagram.com")
sleep(7)
username=driver.find_element(By.NAME, "username")
username.clear()
username.send_keys("") #input your username
password=driver.find_element(By.NAME, "password")
password.clear()
password.send_keys("") #input the password

login=driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]").click()
sleep(10)

notification=driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()

notification2=driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()

insta_data=[]

driver.refresh()
sleep(4)

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
wait = WebDriverWait(driver, rd.randint(7,12))
import os
import wget
import urllib.request
import requests


def keywordSearch(keyword):
    path = os.getcwd()
    path = os.path.join(path, keyword[1:] + "s")
    os.mkdir(path)
    counter = 0
    #for _ in range(5):
    for i in range(1, 4):
        for j in range(1, 4):
            sleep(rd.randint(1,4))
            big_div_img = driver.find_element(By.XPATH, f"//*[@id='mount_0_0_W6']/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div/div/div/div[{i}]/div[{j}]")
            image_field = wait.until(EC.element_to_be_clickable(big_div_img.find_element(By.CLASS_NAME, '_aagw'))).click()
            sleep(rd.randint(1,7))
            
            div_image = big_div_img.find_element(By.CLASS_NAME, '_aagv')
            image = div_image.find_element(By.TAG_NAME, 'img')
            source = image.get_attribute('src')
            alt = image.get_attribute('alt')
                
            sleep(rd.randint(1,4))
            #save image
            save_as = os.path.join(path, keyword[1:] + str(counter) + '.jpg')
            wget.download(source, save_as)
            sleep(rd.randint(2,6))
            counter += 1
                

                
            try:
                subject_username = driver.find_element(By.XPATH, "//*[@id='mount_0_0_W6']/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/div/div/div/span/a").text
            except:
                driver.execute_script("window.history.go(-1)")
                continue
                                                        
            pic_desc = driver.find_element(By.XPATH, "//*[@id='mount_0_0_W6']/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/div/li/div/div/div[2]/div[1]/span").text

                                                                    
            insta_data.append((keyword, source, alt, subject_username, pic_desc))
            
            driver.execute_script("window.history.go(-1)")


        #driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(3) ## to give pause so that page loads properly


hashtags = ["#thrift", "#thriftshop", "#thriftstore", "#thriftstorefinds", "#thriftfinds", "#thriftlebanon", "#lebanonthrift", "#handpicked", "#thriftedfashion", "#brandthrift", "#reuse", "#recycle", "#used", "#usedbrands", "#secondhandlebanon", "#preownedlebanon"]


for hT in hashtags:
    explore = driver.find_element(By.XPATH, "//a[@href='/explore/']").click()
    sleep(rd.randint(4,6))
    searchbox = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search']")
    searchbox.clear()
    searchbox.send_keys(hT)
    searchbox.send_keys(Keys.RETURN)
    sleep(rd.randint(4,6))
    searchbox.send_keys(Keys.RETURN)
    searchbox.send_keys(Keys.RETURN)
    sleep(rd.randint(4,6))
    keywordSearch(hT)



import pandas as pd
df = pd.DataFrame(insta_data, columns=['keyword', 'source', 'alt', 'subject_username', 'pic_desc'])
df.to_csv(r'') #your wanted path for CSV file

df
