import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
service = Service("choremedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("C:/Users/yetki/OneDrive/Masaüstü/Selenium/9-alıştırma-boot/index.html")


def siparisver():
    driver.find_element(By.CLASS_NAME, "buy").click()


def mesajoku():
    return driver.find_element(By.ID, "mesaj")


isim = driver.find_element(By.ID, "name")
boy = driver.find_element(By.ID, "md")
extra = driver.find_element(By.NAME, "Z")
dropdown = driver.find_element(By.ID, "payi")
odeme = Select(dropdown)
odeme_tipleri = odeme.options
sekil = odeme.select_by_index[1]
siparisver()
if (isim.is_selected() == False):
    print("İsim Alanı Boş")

isim.send_keys("tom cruise")
print("isim alanı girildi ")

boy.click()
print("Boy girildi")
print("")
time.sleep(5)

# driver.execute_script("window.history.go(-1)")


"""
dongu = True
while (dongu):
    isim = driver.find_element(By.ID, "name")
    boy = driver.find_element(By.NAME, "fav_language")
    extra = driver.find_element(By.NAME, "Z")
    dropdown = driver.find_element(By.ID, "pay")
    odeme = Select(dropdown)
    odeme_tipleri = odeme.options
    isim.send_keys("yetkin")
    print(isim.is_selected())
    print(boy.is_selected())
    print(extra.is_selected())
    time.sleep(5)
    dongu = False
"""
