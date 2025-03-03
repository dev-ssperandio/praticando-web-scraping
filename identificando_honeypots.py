from time import sleep
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Atibuindo o caminho para o driver do Chrome
DRIVER_PATH = "./chromedriver-win64/chromedriver.exe"

# Configurando opções
options = Options()
# options.add_argument('--headless') # Oculta o navegador
# options.add_argument('--window-size=1920,1200') # Dimensiona o navegador

service = Service(DRIVER_PATH)

# driver = webdriver.Chrome(service=service, options=options)

with webdriver.Chrome(service=service, options=options) as driver:
    # Honeypot é um tipo de bloqueador de bot que utiliza elementos escondidos do usuário comum
    # se não forem tratados corretamente, poderão ser interagidos pelas automações
    driver.get("https://www.dio.me/en/sign-up")

    placeholders = {
        "*Full name": "Sidney R. Sperandio",
        "*Your best e-mail": "dev.ssperandio@gmail.com",
        "+55 (99) 99999-9999": "11999990000",
        "*Password": "12345678",
    }

    input_elements = driver.find_elements(By.TAG_NAME, "input")

    for input_element in input_elements:
        placeholder = input_element.get_attribute("placeholder")

        if placeholder:
            if input_element.is_displayed():
                input_element.send_keys(placeholders[placeholder])
        else:
            print("Encontramos o honeypot!")

    sleep(5)
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))
    )
    submit_button.click()
    sleep(5)

# driver.quit()
