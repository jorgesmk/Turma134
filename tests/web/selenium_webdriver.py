# Configura
# Biblioteca / Imports

# Dados de Entrada
from selenium import webdriver
from selenium.webdriver.common.by import By

origem = 'São Paolo'
destino = 'New York'
primeiro_nome = 'Juca'
bandeira = 'American Express'
lembrar_de_mim = True

# Resultado Esperado
titulo_passagens_esperado = 'Flights from São Paolo to New York:'
mensagem_agradecimento_esperada = 'Thank you for your purchase today!'
preco_passagem_esperado = '555 USD'

# Executa
class Testes:
   # Início
    def setup_method(self):
        # instanciar a biblioteca/motor/engine
        # informar onde está o WebDriver
        self.driver = webdriver.Chrome(
            'C:\\Users\\lynna\\PycharmProjects\\134inicial\\vendors\\Drivers\\chromedriver102.exe'
        )
    # Fim
    def teardown_method(self):
        # destruir o objeto da biblioteca utilizada
        self.driver.quit()

    # Meio
    def testar_comprar_passagem(self):
        # e2e / end to end / ponta a ponta
        # Pagina inicial (home)
        # Executa / Valida
        # abrir o browser no endereco
        self.driver.get('https://www.blazedemo.com')
        dropdown = self.driver.find_element(By.NAME, "fromPort")
        dropdown.click()
        dropdown.find_element(By.XPATH, '//option[ .= "São Paolo"]').click()
        dropdown = self.driver.find_element(By.NAME, 'toPort')
        dropdown.click()
        dropdown.find_element(By.XPATH, '//option[ .= "New York"]').click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()

        # Pagina lista de passagens

        # Pagina de Compras

        # Pagina de Obrigado

    # Valida
