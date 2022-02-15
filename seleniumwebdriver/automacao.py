from selenium import webdriver
import time
import scrapy


navegador = webdriver.Chrome()
navegador.get("http://portal.trf5.jus.br/cp/")
time.sleep(1)

navegador.find_element_by_xpath('//*[@id="filtro"]').send_keys("00156487819994050000")
time.sleep(1)
navegador.find_element_by_xpath('//*[@id="submitConsulta"]').click()
time.sleep(1)

