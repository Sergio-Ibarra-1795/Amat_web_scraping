from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time
import json


def get_table_information(operator_name):
    rows = driver.find_elements(By.XPATH, "//table[@id='table']/tbody/tr")
    period_dict = {}
    operator_periods = []    
    for row in rows:
        period_dict['period'] = row.find_element(By.XPATH, ".//td[1]").text
        period_dict['name'] = row.find_element(By.XPATH, ".//td[2]").text
        period_dict['active'] = row.find_element(By.XPATH, ".//td[3]").text
        period_dict['clients'] = row.find_element(By.XPATH, ".//td[4]").text
        period_dict['investment_funds'] = row.find_element(By.XPATH, ".//td[5]").text

        json_operator = json.dumps(period_dict)
        operator_periods.append(json_operator)
        print(json_operator)

    with open(f'{operator_name}.json', 'a') as json_file:
        for operator in operator_periods:
            json_file.write(operator)
            json_file.write(',\n')

  
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://amibrevalidacion.amib.com.mx:8080/srifi/#/consultas/InformacionOperadora")

time.sleep(6)


periods = driver.find_elements(By.XPATH, "//select[@id='idPeriodoMensual']/option")
del periods[0]

for period in periods:
    print(period.text)

    select_1 = Select(driver.find_element(By.XPATH, "//select[@id='idPeriodoMensual']"))
    select_1.select_by_visible_text(period.text)

    button = driver.find_element(By.XPATH, "//button[@class='btn btn-default']")
    button.click()

    time.sleep(7)

    get_table_information(period.text)

    try:
        page_last = driver.find_element(By.XPATH, "//li[@class='page-last']/a")
        page_last2 = int(page_last.text)
    except:
        pages_count = driver.find_elements(By.XPATH, "//li[@class='page-number']")
        page_last2 = len(pages_count) + 1

    pages = range(page_last2)
    for page in pages:
        if page == (page_last2 - 1) :
            print('se cosechó')
            link = driver.find_element(By.XPATH, "//li[@class='page-next']/a")    
            link.click()            
        else:    
            link = driver.find_element(By.XPATH, "//li[@class='page-next']/a")    
            link.click()
            #time.sleep(2)
            get_table_information(period.text)


driver.close()

