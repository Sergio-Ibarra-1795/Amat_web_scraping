from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time
import json


def get_table_information():
    rows = driver.find_elements(By.XPATH, "//tbody[@class='list-tbody async-list-tbody']/tr")
    rows_number = len(rows)
    all_rows = range(1, rows_number + 1)
    for row in all_rows:
        page = driver.find_element(By.XPATH, f"//tbody[@class='list-tbody async-list-tbody']/tr[{row}]")
        get_page_information(page)

    try:
        next_page = driver.find_element(By.XPATH, "//a[@class='NavBtnForward']")
        next_page.click()
        time.sleep(6)
        get_table_information()
    except:
        pass        


def get_page_information(page):
    ad_link = page.find_element(By.XPATH, ".//td[4]/a")
    ad_link.click()
    time.sleep(6)

    page_dict = {}
    page_dict['file'] = driver.find_element(By.XPATH, "//div[@class='subtitle_01 maintitle']").text
    page_dict['file_code'] = driver.find_element(By.XPATH, "//ul/li[1]/div[@class='form_answer']").text
    page_dict['file_description'] = driver.find_element(By.XPATH, "//ul/li[2]/div[@class='form_answer']").text
    page_dict['file_reference'] = driver.find_element(By.XPATH, "//ul/li[3]/div[@class='form_answer']").text
    page_dict['file_type'] = driver.find_element(By.XPATH, "//ul/li[4]/div[@class='form_answer']").text
    page_dict['file_category'] = driver.find_element(By.XPATH, "//ul/li[5]/div[@class='form_answer']").text
    page_dict['file_state'] = driver.find_element(By.XPATH, "//div[@class='form_container'][2]/ul/li[4]/div[2]").text
    page_dict['file_publication'] = driver.find_element(By.XPATH, "//div[@class='form_container'][2]/ul/li[5]/div[2]").text
    page_dict['file_validity'] = driver.find_element(By.XPATH, "//div[@class='form_container'][2]/ul/li[6]/div[2]").text
    page_dict['file_buying'] = driver.find_element(By.XPATH, "//div[@class='form_container'][3]/ul/li[1]/div[2]").text

    json_page = json.dumps(page_dict)

    with open('convocatorias_completas.json', 'a') as json_file:
        json_file.write(json_page)
        json_file.write(',\n')


    back_button = driver.find_element(By.XPATH, "//a[@title='Volver a la Lista']")
    back_button.click()
    time.sleep(6)


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://compranet.hacienda.gob.mx/esop/guest/go/public/opportunity/current?locale=es_MX")

time.sleep(6)

get_table_information()


driver.close()

