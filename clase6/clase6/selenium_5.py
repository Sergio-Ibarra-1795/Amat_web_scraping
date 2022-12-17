# Ejercicio de scraping
# Autor: Goz
# Descripción: Descargar contenido de un sitio web con selenium
#    

import json
import time

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://hoopshype.com/salaries/players/")

players_links = driver.find_elements(By.XPATH, '//td[@class="name"]/a')
links = []
all_players = []

for p in range(51):
    links.append(players_links[p].get_attribute('href'))

for link in links:
    driver.get(link)
    player = {}
    try:
        player_fullname = driver.find_element(By.XPATH, '//div[@class="player-fullname"]')
        player['fullname'] = player_fullname.text
    except:
        player['fullname'] = ""
        pass
    try:
        player_team = driver.find_element(By.XPATH, '//div[@class="player-team"]')
        player['team'] = player_team.text
    except:
        player['team'] = ""
        pass 
    try:
        rows = driver.find_elements(By.XPATH, '//span[@class="player-bio-text-line-value"]')
        player['position'] = rows[0].text
        player['born'] = rows[1].text
        player['height'] = rows[2].text
        player['weight'] = rows[3].text
        player['salary'] = rows[4].text
    except:
        player['position'] = ""
        player['born'] = ""
        player['height'] = ""
        player['weight'] = ""
        player['salary'] = ""
        pass                
    json_player = json.dumps(player)
    all_players.append(json_player)
    print(json_player)
    time.sleep(2)
    
with open('nba_players.json', 'a') as json_file:
    json_file.write("[\n")
    for player in all_players:
        json_file.write(player)
        json_file.write(',\n')
    json_file.write("]\n")

driver.close()
