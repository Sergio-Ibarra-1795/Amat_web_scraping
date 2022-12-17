from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time
import json


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://amibrevalidacion.amib.com.mx:8080/srifi/#/consultas/InformacionOperadora")

time.sleep(6)

operators = driver.find_elements(By.XPATH, "//select[@id='idOperadora']/option")
del operators[0]

for operator in operators:
    print(operator.text)

    select_2 = Select(driver.find_element(By.XPATH, "//select[@id='idOperadora']"))
    select_2.select_by_visible_text(operator.text)

    button = driver.find_element(By.XPATH, "//button[@class='btn btn-default']")
    button.click()

    time.sleep(7)
    operator_dict = {}
    operator_periods = []

    rows = driver.find_elements(By.XPATH, "//table[@id='table']/tbody/tr")
    for row in rows:

        operator_dict['period'] = row.find_element(By.XPATH, ".//td[1]").text
        operator_dict['name'] = row.find_element(By.XPATH, ".//td[2]").text
        operator_dict['active'] = row.find_element(By.XPATH, ".//td[3]").text
        operator_dict['clients'] = row.find_element(By.XPATH, ".//td[4]").text
        operator_dict['investment_funds'] = row.find_element(By.XPATH, ".//td[5]").text
    
        json_operator = json.dumps(operator_dict)
        operator_periods.append(json_operator)
        print(json_operator)

    with open(f'{operator.text}.json', 'a') as json_file:
        json_file.write("[\n")
        for operator in operator_periods:
            json_file.write(operator)
            json_file.write(',\n')
        json_file.write("]\n")




driver.close()

