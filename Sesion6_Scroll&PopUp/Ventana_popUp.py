import json
import time

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#Encendemos el navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#Abrimos la pagina con la URL 
driver.get("https://www.drayage.com/directory/results.cfm?city=SAV&port=y&OceanCntrs=y&drvrs=y&showClicks=y")
## dirver.window_handles Nos permite manejar ventanas
## Estamos nombrando a la ventana en la que estamos (ventana original)
window_before = driver.window_handles[0]
time.sleep(3)

rows = driver.find_elements(By.XPATH, '//table[@align="center"]/tbody/tr/td/table/tbody/tr')

for row in rows:
    company = {}
    try:
        company_link = row.find_element(By.XPATH, './/td[15]/a')
        company_link.click()
        time.sleep(2)
        ##Abrimos la ventana que sale y la inicializamos en una nueva variable
        window_after = driver.window_handles[1]
        ##Vamos a cambiarnos a la nueva ventana
        ##Con esto ya estamos en la ventana que se abrió con cada enlace
        driver.switch_to.window(window_after)

        #Obtengo la primera tabla dentro del detalle de cada link
        table = driver.find_element(By.XPATH, '//table[1]/tbody')
        company['name'] = table.find_element(By.XPATH, '//tr[2]/td[2]').text
        ##Los demas detalles se obtiene por su nombre
        try:
            company['phone'] = driver.find_element(By.XPATH, '//td[contains(text(),"Phone:")]/following-sibling::td[1]').text
        except:
            company['phone'] = 's/n'
        try:
            company['description'] = driver.find_element(By.XPATH, '//td[contains(text(),"Company Description:")]/following-sibling::td[1]').text
        except:
            company['description'] = 's/n'
        
        json_company = json.dumps(company)
        with open('companies.json', 'a') as json_file:
            json_file.write(json_company)
            json_file.write('\n')

        time.sleep(3)
        driver.close()
        driver.switch_to.window(window_before)
        print(company['name'])
        print('*************')


    except:
        print('Link de compañia no encontrado')

driver.quit()