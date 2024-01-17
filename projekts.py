import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import openpyxl
from openpyxl import Workbook, load_workbook

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

url = "https://www.ss.com/lv/transport/cars/"
driver.get(url)
time.sleep(2)

find = driver.find_element(By.LINK_TEXT, "Mercedes")
find.click()
time.sleep(2)

find = driver.find_element(By.LINK_TEXT, "Meklēšana")
find.click()
time.sleep(2)

find = driver.find_element(By.ID, "ptxt")
find.clear()
find.send_keys("Cls")
time.sleep(3)
find.send_keys(Keys.RETURN)

price_list = []
tilp_list = []
nobr_list = []
gad_list = []
mod_list = []

o = 4
i = 0
while i <= 34:
    x = driver.find_elements(By.CLASS_NAME, "amopt")

    if o >= len(x):
        break

    cena = x[o]
    car_price = cena.text
    price_list.append(car_price)
    o = o + 5
    i += 1

o = 3
i = 0
while i <= 34:
    x = driver.find_elements(By.CLASS_NAME, "amopt")

    if o >= len(x):
        break

    nobr = x[o]
    nobr_text = nobr.text
    nobr_list.append(nobr_text)
    o = o + 5
    i += 1

o = 2
i = 0
while i <= 34:
    x = driver.find_elements(By.CLASS_NAME, "amopt")

    if o >= len(x):
        break

    tilp = x[o]
    tilp_text = tilp.text
    tilp_list.append(tilp_text)
    o = o + 5
    i += 1

o = 1
i = 0
while i <= 34:
    x = driver.find_elements(By.CLASS_NAME, "amopt")

    if o >= len(x):
        break

    gads = x[o]
    gads_text = gads.text
    gad_list.append(gads_text)
    o = o + 5
    i += 1

o = 0
i = 0
while i <= 34:
    x = driver.find_elements(By.CLASS_NAME, "amopt")

    if o >= len(x):
        break

    mod = x[o]
    mod_text = mod.text
    mod_list.append(mod_text)
    o = o + 5
    i += 1

print(price_list)

input()