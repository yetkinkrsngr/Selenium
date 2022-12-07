
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
service = Service("choremedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("C:/Users/yetki/OneDrive/Masaüstü/Selenium/7-radyo-dugmesi/index.html")

dropdown = driver.find_element(By.ID, "pay")
odeme = Select(dropdown)
odeme_tipleri = odeme.options  # web element listesi her bir option tagi için

for tip in odeme_tipleri:
    print(tip.text)
