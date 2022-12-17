from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time
import urllib.request
import json

licitation_type = "ESTATAL"
licitation_year = "2022"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://sop.chiapas.gob.mx/licitaciones.php")
time.sleep(6)

options = driver.find_elements(By.XPATH, "//select[@name='licitacion']/option")
del options[0]

for option in range(len(options)):
    licitation_dict = {}
    options2 = driver.find_elements(By.XPATH, "//select[@name='licitacion']/option")
    del options2[0]

    time.sleep(3)
    select_1 = Select(driver.find_element(By.XPATH, "//select[@name='tipolicitacion']"))
    select_1.select_by_visible_text(licitation_type)
    time.sleep(1)
    select_2 = Select(driver.find_element(By.XPATH, "//select[@name='yearlicitacion']"))
    select_2.select_by_visible_text(licitation_year)
    time.sleep(1)
    select_3 = Select(driver.find_element(By.XPATH, "//select[@name='licitacion']"))
    select_3.select_by_visible_text(f"{options2[option].text}")
    time.sleep(1)

    button = driver.find_element(By.XPATH, "//button[@id='buscartodo']")
    button.click()
    time.sleep(2)

    licitation_dict['title'] = driver.find_element(By.XPATH, "//blockquote").text
    licitation_dict['licitation'] = driver.find_element(By.XPATH, "//ul[@class='list-group']/li[1]").text
    licitation_dict['visit'] = driver.find_element(By.XPATH, "//ul[@class='list-group']/li[2]/p").text
    licitation_dict['reunion'] = driver.find_element(By.XPATH, "//ul[@class='list-group']/li[3]/p").text
    licitation_dict['economic'] = driver.find_element(By.XPATH, "//ul[@class='list-group']/li[4]/h3").text.replace('APERTURA DE PROPUESTA TÉCNICA - ECONÓMICA', '')
    licitation_dict['licitation_start'] = driver.find_element(By.XPATH, "//ul[@class='list-group']/li[5]/p/strong").text
    licitation_dict['licitation_end'] = driver.find_element(By.XPATH, "//ul[@class='list-group']/li[6]/p/strong").text
    licitation_dict['days'] = driver.find_element(By.XPATH, "//ul[@class='list-group']/li[7]/p/strong").text
    licitation_dict['licitation_file'] = f"convocatoria_{licitation_dict['licitation']}.pdf"

    json_licitation = json.dumps(licitation_dict)
    print(json_licitation)

    licitation_file = driver.find_element(By.XPATH, "//img[@alt='Image Description']/parent::a[1]")
    licitation_file_url = licitation_file.get_attribute('href')
    print(f"Descargando {licitation_file.get_attribute('href')}")
    urllib.request.urlretrieve(licitation_file_url, f"/home/goz/Courses/web_scraping/practica_1/clase3/selenium/convocatoria_{licitation_dict['licitation']}.pdf")
    print('Convocatoria descargada!')
    time.sleep(5)

    with open(f'licitaciones_{licitation_type}_{licitation_year}.json', 'a') as json_file:
        json_file.write(json_licitation)
        json_file.write(',\n')

driver.close()


