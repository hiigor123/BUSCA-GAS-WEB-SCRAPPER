from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("C:\chromedriver")
#LISTA DE ENDEREÇOS DAS LOJAS
lista_endereco = ['','']
#PRA CADA ENDEREÇO BUSQUE OS VALORES DE BOTIJAO
for endereco in lista_endereco:
    #SITE DA BUSCA
    driver.get("https://chama.com.br/")
    #SLEEP PRA DAR UMA PAUSA NO PROCESSAMENTO ENTRE AS TAREFAS
    #ISSO FOI FEITO POIS ALGUNS SITES NÃO PERMITEM CLICKS RÁPIDOS EM POUCOS MILESEGUNDOS
    time.sleep(5)
    #CLICA NO CAMPO DE DEXTO    
    driver.find_element_by_id("searchTextField").click()
    #DIGITA O ENDEREÇO DA VEZ
    time.sleep(2)
    driver.find_element_by_id("searchTextField").send_keys(endereco)
    #APERTA ENTER PRA PESQUISAR
    time.sleep(5)
    driver.find_element_by_id("searchTextField").send_keys(Keys.ENTER)
    #SLEEP PARA CARREGAR A LISTA
    time.sleep(20)
    #LAÇO DE REPETIÇÃO PARA CONVERTER LISTA HTML PARA TEXT SEPARADO POR VIRGULA
    html_list = driver.find_element_by_class_name("OfferOptionsList_list__eDUg7")
    items = html_list.find_elements_by_tag_name("li")
    for item in items:
        text = item.text
        text = text.replace('\n',';')
        print (endereco + ";" + text)

    time.sleep(3)
