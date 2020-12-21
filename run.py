from selenium import webdriver

path = "C:/Users/KIM/Desktop/kilho/python/kakao/ksupload/chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get("https://www.google.com")
print(driver.title)

search = driver.find_element_by_name("s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

main = driver.find_element_by_id("main")
prinT(main.text)

driver.quit()