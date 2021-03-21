from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import requests
import urllib.request
import sys
import os
import datetime

#get day of the week
date = datetime.datetime.today().weekday()
week   = ['luni','marti','miercuri','joi','vineri','sambata','duminica']
ziua_saptamanii = week[date]

#scrape image of cafeluta
site = 'https://www.google.com/search?tbm=isch&q=cafeluta de '+ziua_saptamanii

#providing driver path
driver = webdriver.Firefox()

#passing site url
driver.get(site)

#parsing
soup = BeautifulSoup(driver.page_source, 'html.parser')

#closing web browser
driver.close()

#scraping image urls with the help of image tag and class used for images
images_of_cafeluta = soup.find_all("img", class_="rg_i")
urllib.request.urlretrieve(images_of_cafeluta[0]['src'], "cafelute/" + ziua_saptamanii+".jpg")


#login into facebook
#set options to get rid of annoying pop-ups
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 1 
})

#create driver with wanted options
test_driver=webdriver.Chrome(chrome_options=option)

#open website
test_driver.get("http://www.facebook.com/messages")

#find and save login fields
email_input = test_driver.find_element_by_id("email")
password_input=test_driver.find_element_by_id("pass")
login_button=test_driver.find_element_by_id("u_0_2")

#set login data
email="your_email"
password="your_password"

#fill in login fields and press login button
email_input.send_keys(email)
password_input.send_keys(password)
login_button.click()

#write in the search by name area
contacts= ["Aghenitei Bianca","Andreea Nechita","Roberta Corfu","Zoican Denis"]


for contact in contacts: 
    time.sleep(5)
    search_input=test_driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div/div[1]/div[2]/div[3]/div/div[1]/div/div/div[1]/span[1]/label/input")
    search_input.send_keys(contact)

    #click on the first account 
    time.sleep(2)
    first_account=test_driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div/div[1]/div[2]/div[3]/div/div[1]/div/div/div[1]/span[1]/div/div/div[2]/ul/li/a")
    first_account.click()

    #writing a message
    time.sleep(2)
    message= "Buna buna! ^_^ Sunt eu in carne si oase si m-am trezit sa iti urez o dimineata frumoasa si sa ai o zi productiva, " + contacts[0] + "! No talk to me im cranky ;P "
    message_text_box = test_driver.find_element_by_css_selector('.notranslate')
    message_text_box.send_keys(message)

    #hit send
    time.sleep(2)
    send_button=test_driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/span/div[2]/div[2]/div[2]/div[1]/a")
    send_button.click()

    #send image of cafeluta
    time.sleep(1)
    image_path = "cafelute/" + ziua_saptamanii + ".jpg"
    image_input = test_driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/span/div[2]/div[2]/div[2]/div/div[3]/div[2]/form/div/span/input")
    image_input.send_keys(image_path)

    #hit send
    time.sleep(2)
    send_button=test_driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/span/div[2]/div[2]/div[2]/div/a")
    send_button.click()




