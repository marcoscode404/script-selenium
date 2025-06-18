import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Inicializa o navegador com o ChromeDriver
URL = "https://ui.nuxt.com/"

for i in range(3):
    print(f"Execução {i + 1}...")
    # Inicializa o navegador
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # Abre a página
    driver.get(URL)
    # Espera 5 segundos
    time.sleep(5)
    # Fecha o navegador
    driver.quit()
    print(f"Execução {i + 1} finalizada.\n")






# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# # Abre a página
# driver.get("https://www.r7.com/")

# # Espera 5 segundos
# time.sleep(5)

# # Fecha o navegador
# driver.quit()



