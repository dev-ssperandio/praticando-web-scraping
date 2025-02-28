from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


# Configura o caminho para o Chromedriver
DRIVER_PATH = './chromedriver-win64/chromedriver.exe'

# Configura opções do Chrome
options = Options()
options.add_argument("--headless") # Habilita modo handles
options.add_argument("--window-size=1920,1200") # Configura a dimensão da janela


# Inicializa o servidor do ChromeDriver
service = Service(DRIVER_PATH)
# Inicializa o navegador com o serviço e opções do ChromeDriver
driver = webdriver.Chrome(service=service, options=options)

# Navegar para a URL
driver.get('https://news.ycombinator.com/')

# Recupera o código-fonte da página
html = driver.page_source

# # Localiza o terceiro elemnto 'td' do primerio elemento 'tr' o qual possui o título do artigoe o link
# title_element = driver.find_element(By.XPATH, '//tr[@id="43207831"]/td[3]/span/a') 

# # Extrai e exibe o texto para localizaçõa do WebElement
# print(title_element.text)

# # Clica no link para navegar até o página do artigo
# title_element.click()

# # Opcional, aguardar a nova página carregar e executar a ação
# # Para demonstração, exibe a URL atual depois do click
# print(driver.current_url)

# # Exibir o código-fonte da página no console
# print(driver.page_source)

# É uma boa pratica fechar o navegador quando consluído
driver.quit()

# Analisa o HTML com BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Encontra todos os elementos 'tr' com a classe 'athing' o qual contém os títulos de notícias
titles = soup.find_all('tr', class_='athing')

# Itera sobre cada título e os exibe
for title in titles:
    # Encontra a tag <a> dentro do span 'titleline' dentro de um 'td' com a classe 'title'
    title_link = title.find('td', class_='title').find('span', class_='titleline').find('a')
    title_text = title_link.get_text() # Extrai o texto do título
    print(title_text)


# with webdriver.Chrome(executable_path=DRIVER_PATH) as driver:
#     ...
