import requests
from bs4 import BeautifulSoup
import selenium
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from getpass import getpass

usr=getpass('Enter Email Id:') 
pwd=getpass('Enter Password:') 

driver = webdriver.Chrome()
driver.get('https://www.facebook.com/')

username_box = driver.find_element(By.ID, 'email')
username_box.send_keys(usr)
print ("Email Id entered")
sleep(1)
 
password_box = driver.find_element(By.ID, 'pass')
password_box.send_keys(pwd)
sleep(1)

login_box = driver.find_element(By.ID, 'loginbutton')
login_box.click()

sleep(3)

input("Verify your identity on your mobile device. Wait for the FB Homepage to appear. Press Enter to continue...")

sleep(5)

url = 'https://meta.ai'
driver.get(url)
i = 2
prompt = ''

sleep(5)

while prompt.lower() != 'exit':
    prompt = input("What is your prompt ?")
    print()
    search_box = driver.find_element(By.TAG_NAME, "textarea")
    search_box.send_keys(prompt)
    sleep(1)
    search_box.send_keys(Keys.RETURN)

    if i == 2:
        input("Please click on connect with Facebook. Press Enter to continue...")
    else:
        pass

    sleep(10)

    try:
        output = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[1]/div/div/div/div/div/div[' + str(i) + ']/div/div/div[2]/div[1]/div').text
        while output == 'Searching...': #Gives more time to the AI to generate the answer
            sleep(5)
            output = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[1]/div/div/div/div/div/div[' + str(i) + ']/div/div/div[2]/div[1]/div').text

        print('Meta AI : ' + output)
        print()
    except:
        print("Could not retrieve response")
        print()

    
    i = i + 2

driver.close()