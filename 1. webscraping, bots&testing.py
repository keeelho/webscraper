from selenium import webdriver

path = "C:/Users/KIM/Desktop/kilho/python/kakao/ksupload/chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://www.google.com")
print(driver.title)
driver.quit()