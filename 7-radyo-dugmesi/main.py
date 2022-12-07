import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service = Service("choremedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()


driver.get("C:/Users/yetki/OneDrive/Masaüstü/Selenium/7-radyo-dugmesi/index.html")
middle_size = driver.find_element(By.ID, "md")
Olive = driver.find_element(By.ID, "Olive")
Mantar = driver.find_element(By.ID, "Mantar")
print(middle_size.is_selected())
print(Olive.is_selected())
print(Mantar.is_selected())
middle_size.click()
Olive.click()
Mantar.click()
print(middle_size.is_selected())
print(Olive.is_selected())
print(Mantar.is_selected())
kapanma = input()
