from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://tr.wikipedia.org/wiki/Anasayfa")
# aranacak madde bulunur
seckin_madde_alani = driver.find_element(By.ID, "mp-tfa")
# o madde text haline getirilir
seckin_madde_yazisi = seckin_madde_alani.text
# liste haline getirilip 0 indexdeki eleman yazdırılır.
seckin_madde_yazisi = seckin_madde_yazisi.split(";")[0]
print(seckin_madde_yazisi)
# burada ise daha kısa farklı bir alana ulaştık.
kaliteli_madde = driver.find_element(By.ID, "mf-tfp")
kaliteli_madde = kaliteli_madde.text.split(",")[0]
print(kaliteli_madde)
