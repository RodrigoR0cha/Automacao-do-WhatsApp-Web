#Importar as bibliotecas
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys 

# Navegar até o whatsapp web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(30)

# Definir contatos, grupos e mensagens a ser enviada

contatos = ['Patrícia', 'Vanderlan', 'Rodrigo', 'Marlucia']

mensagem = 'Olá é apenas um teste, minha primeira automação de whatsapp!!'
            

# Buscar contatos/ grupos

def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

# Campo de mensagem privada 'copyable-text selectable-text'

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)    



# Enviar mensagens para o contato/grupo

for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)







