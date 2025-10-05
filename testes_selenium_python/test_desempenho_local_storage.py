from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://qa.medcloud.link")

# Ver localStorage
local_storage = driver.execute_script("return window.localStorage;")
print("LocalStorage:", local_storage)

# Ver sessionStorage
session_storage = driver.execute_script("return window.sessionStorage;")
print("SessionStorage:", session_storage)

driver.quit()
