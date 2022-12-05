
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# By elementini ekledik
from selenium.webdriver.common.by import By
# time klası eklendi
import time
service = Service("choremedriver.exe")
driver = webdriver.Chrome(service=service)
# get ile siteye gidilir
driver.get("http:/www.google.com")
# tam ekran yapma
driver.maximize_window()
# find elemment ile input bulunur
seachbar = driver.find_element(By.CLASS_NAME, "gLFyf")
#seachbar = driver.find_element(By.NAME, "q")
# send keys ile google ara inputune istediğimiz giriş yapılır
seachbar.send_keys("usd To try")
# 2 saniye bekletilir
bekle = time.sleep(2)
# enter tuşu
# seachbar.send_keys(Keys.Enter)
seachbar.submit()
# istediğimiz link bulunur
seachbar = driver.find_element(By.CLASS_NAME, "LC20lb")
# link tıklanır
seachbar.click()


bekle = time.sleep(10)
