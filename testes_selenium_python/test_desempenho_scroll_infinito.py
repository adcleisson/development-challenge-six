from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://qa.medcloud.link")
driver.maximize_window()

altura_total = driver.execute_script("return document.body.scrollHeight")
passo = 500 
posicao = 0

while posicao < altura_total:
    driver.execute_script(f"window.scrollTo(0, {posicao});")
    posicao += passo
    time.sleep(0.5) 