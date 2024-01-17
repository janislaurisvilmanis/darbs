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

input()