from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time
import json


def get_table_information():
    rows = driver.find_elements(By.XPATH, "//tbody[@class='list-tbody async-list-tbody']/tr")
    ad_dict = {}
    ads_list = []    
    for row in rows:
        ad_dict['number'] = row.find_element(By.XPATH, ".//th[1]").text
        ad_dict['buying_unit'] = row.find_element(By.XPATH, ".//td[2]").text
        ad_dict['file_reference'] = row.find_element(By.XPATH, ".//td[3]").text
        ad_dict['file_description'] = row.find_element(By.XPATH, ".//td[4]").text
        ad_dict['contract'] = row.find_element(By.XPATH, ".//td[5]").text
        ad_dict['term'] = row.find_element(By.XPATH, ".//td[6]").text

        json_ad = json.dumps(ad_dict)
        ads_list.append(json_ad)
        print(json_ad)

    with open('vigentes.json', 'a') as json_file:
        for ad in ads_list:
            json_file.write(ad)
            json_file.write(',\n')

    try:
        next_page = driver.find_element(By.XPATH, "//a[@class='NavBtnForward']")
        next_page.click()
        time.sleep(7)
        get_table_information()
    except:
        pass

  
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://compranet.hacienda.gob.mx/esop/guest/go/public/opportunity/current?locale=es_MX")

time.sleep(6)

get_table_information()







driver.close()

