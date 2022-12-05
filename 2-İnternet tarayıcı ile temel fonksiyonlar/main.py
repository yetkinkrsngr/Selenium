from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("choremedriver.exe")
driver = webdriver.Chrome(service=service)
# get metotdu istediğimiz sayfaya gidiyoruz.
driver.get("http://www.apple.com")
driver.save_screenshot("assets/apple.png")
# current_url ise url sini çeker.
title = driver.current_url
# apple dosyası içinde apple.com olduğu için girdi.
if "apple.com" in title:
    print("suanki baslık : "+title)
# açılan pencere küçük olduğundan büyütmemiz gerekirse diye.
driver.maximize_window()

driver.get("http://www.google.com")
# aşağıda sayfanın ekran görüntüsünü aldık
driver.save_screenshot("assets/google.png")
title = driver.current_url
# title ise title htmlsini çeker.
baslık = driver.title
baslık2 = baslık.lower()
if "google.com" in title:
    print("suanki baslık : "+baslık)


if "google" in baslık2:
    # bir önceki sayfaya gider.
    driver.back()
    print("tebrikler apple sayfasına geri döndün")
