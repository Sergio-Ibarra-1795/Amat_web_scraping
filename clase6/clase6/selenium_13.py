from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import json


month_year = '08/2022'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.banxico.org.mx/IndicadoresGraficos/actions/graficaDatos/url/li2_in62_op114_mg227_s1/libre/libre?locale=es")
time.sleep(12)

button = driver.find_element(By.XPATH, "//div[@class='drop-down-text']")
button.click()
time.sleep(6)

text_box = driver.find_element(By.XPATH, "//div[@class='text-box search']/input")
text_box.send_keys('12/2022')
time.sleep(7)

check_box2 = driver.find_element(By.XPATH, f"//div[@title='12/2022']/div/div/input")
check_box2.click()
time.sleep(12)

search = driver.find_element(By.XPATH, "//div[@id='app']")
search.click()
time.sleep(6)

button = driver.find_element(By.XPATH, "//div[@class='drop-down-text']")
button.click()
time.sleep(6)

text_box = driver.find_element(By.XPATH, "//div[@class='text-box search']/input")
text_box.send_keys(month_year)
time.sleep(7)

check_box2 = driver.find_element(By.XPATH, f"//div[@title='{month_year}']/div/div/input")
check_box2.click()
time.sleep(12)

search = driver.find_element(By.XPATH, "//div[@id='app']")
search.click()
time.sleep(6)

enter_full_screen = driver.find_element(By.XPATH, "//div[@class='enter-full-screen-mode']")
enter_full_screen.click()
time.sleep(6)

rows = range(29)
columns = range(18)
markets_list = []
markets_list_complete = []

for row in rows:
    day_dict = {}
    day_dict_complete = {}
    for column in columns:
        try:
            cell = driver.find_element(By.XPATH, f"//div[@data-cartesian-positions='{row},{column}']/div/div").text
            print(f'el valor {cell} esta en la posición {row},{column}')
            day_dict[f'pos_{row}_{column}'] = cell
            
            try:
                day = driver.find_element(By.XPATH, f"//div[@data-member='{row + 6}']/div/div").text
                day_dict_complete['day'] = day
            except:
                day_dict_complete['day'] = 'no hay'

            if column == 0:
                day_dict_complete['volumen_total'] = cell
            elif column == 1:
                day_dict_complete['total_swaps'] = cell
            elif column == 2:
                day_dict_complete['24_horas'] = cell
            elif column == 3:
                day_dict_complete['48_horas'] = cell
            elif column == 4:
                day_dict_complete['72_horas'] = cell
            elif column == 5:
                day_dict_complete['96_horas'] = cell
            elif column == 6:
                day_dict_complete['mas_de_96_horas'] = cell
            elif column == 7:
                day_dict_complete['total_operaciones'] = cell
            elif column == 8:
                day_dict_complete['total_contado'] = cell
            elif column == 9:
                day_dict_complete['contado_mismo_dia'] = cell
            elif column == 10:
                day_dict_complete['contado_24_horas'] = cell
            elif column == 11:
                day_dict_complete['contado_48_horas'] = cell
            elif column == 12:
                day_dict_complete['contado_72_horas'] = cell
            elif column == 13:
                day_dict_complete['contado_96_horas'] = cell
            elif column == 14:
                day_dict_complete['futuros'] = cell      
            elif column == 15:
                day_dict_complete['total_forwards'] = cell
            elif column == 16:
                day_dict_complete['forwards_entrega_fisica'] = cell      
            elif column == 17:
                day_dict_complete['forwards_diferencias'] = cell                                                                                                                                                                                                                                                                                                                                                     
        except:
            print(f'NO HAY VALOR en la posición {row},{column}')
            day_dict[f'pos_{row}_{column}'] = "NO VALOR"

    markets_list.append(day_dict)

    if len(day_dict) > 0:     
        markets_list_complete.append(day_dict_complete)


print("La cosecha está lista!!!")

with open(f'{month_year.replace("/","_")}.json', 'a') as json_file:
    for market in markets_list_complete:
      json_page = json.dumps(market)
      if json_page != '{}':
          json_file.write(json_page)
          json_file.write(',\n')

driver.close()

