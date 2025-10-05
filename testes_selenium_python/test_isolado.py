from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://qa.medcloud.link") 

wait = WebDriverWait(driver, 10)

try:
    # Botão "Testar grátis"
    btn_testar = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(text(), 'Testar grátis')]")
    ))
    print("-- Botão 'Testar grátis' encontrado")
    btn_testar.click()
    time.sleep(2)

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.modalDemo")))

    wait.until(EC.visibility_of_element_located((By.ID, "name"))).send_keys("Teste Nome")
    time.sleep(1)
    driver.find_element(By.ID, "email").send_keys("teste@gmail.com")
    time.sleep(1)
    driver.find_element(By.ID, "phone").send_keys("(42)999999999")
    time.sleep(1)

    select_pos = Select(driver.find_element(By.ID, "pos"))
    select_pos.select_by_visible_text("Outros")
    print("-- Opção 'Outros' selecionada no dropdown")
    time.sleep(1)

    btn_enviar = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//button[contains(text(),'Solicitar uma conta grátis para clínica ou hospital')]")
    ))
    btn_enviar.click()
    print("- Formulário enviado")
    time.sleep(2)  

    confirmation = wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "div[role='alert'] span")
    ))
    print("-- Formulário enviado com sucesso! Mensagem detectada:", confirmation.text)
    time.sleep(1)

except Exception as e:
    print("ERRO:", e)

finally:
    driver.quit()
