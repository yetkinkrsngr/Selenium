from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service = Service("choremedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# site açılır
driver.get("https://the-internet.herokuapp.com/login")

# loop diye sonsuz döngü oluşturulur
loop = True

while (loop):
    """aşağıdaki yapı username ve şifre için alanlar bulunur"""
    username_area = driver.find_element(By.ID, "username")
    password_area = driver.find_element(By.ID, "password")
    print("yapmak istediğiniz işlem 1-pozitif test 2-negatif test 3-negeatif test password yanlış 4-negatif test username yanlış çıkmak için herhangi bir tuşa basın.")
    enter = int(input("işlem : "))

    if enter == 1:
        # pozitif test yapılır
        username_area.send_keys("tomsmith")
        password_area.send_keys("SuperSecretPassword!")
        tıkla = driver.find_element(By.CLASS_NAME, "radius")
        tıkla.submit()
        succes = driver.find_element(By.ID, "flash")
        print(succes.text)
        logout = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/a")
        logout.click()
    elif enter == 2:
        # negetif test
        username_area.send_keys("random")
        password_area.send_keys("random")
        tıkla = driver.find_element(By.CLASS_NAME, "radius")
        tıkla.submit()
        failed = driver.find_element(By.ID, "flash")
        print(failed.text)
    elif enter == 3:
        # negetif test
        username_area.send_keys("tomsmith")
        password_area.send_keys("random")
        tıkla = driver.find_element(By.CLASS_NAME, "radius")
        tıkla.submit()
        failed = driver.find_element(By.ID, "flash")
        print(failed.text)
    elif enter == 4:
        # negetif test
        username_area.send_keys("random")
        password_area.send_keys("SuperSecretPassword!")
        tıkla = driver.find_element(By.CLASS_NAME, "radius")
        tıkla.submit()
        failed = driver.find_element(By.ID, "flash")
        print(failed.text)
    else:
        # çıkış
        print("Programdan çıkılıyor.")
        loop = False
