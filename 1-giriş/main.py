# gerekli olan web selnium classları indirildi
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# kullanacağımız chrome servis yolu ve değişkenler atandı
service = Service(".\chromedriver.exe")
driver = webdriver.Chrome(service=service)
# get metodu gideceğimiz siteyi yazarız.
driver.get("https://omercelikten.com/egitim/sifirdan-frontend-gelistirici-egitimi/")
# program kapanmasın diye random giriş istedim.
x = input("gir : ")
