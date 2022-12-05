import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service = Service("choremedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# siteye gideriz
driver.get("https://www.imdb.com/")

# menuye tıklarız
driver.find_element(By.ID, "imdbHeader-navDrawerOpen").click()
# menude en iyi 250 film bulunur ve tıklanır
time.sleep(1)
driver.find_element(
    By.XPATH, "//span[text()='Top 250 Movies']").click()
time.sleep(1)
film_listesi = driver.find_element(
    By.XPATH, "//table/tbody//tr/td[@class='titleColumn']/a")

for i in range(20):
    print(film_listesi[i].text)
driver.quit()
