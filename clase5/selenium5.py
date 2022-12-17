import json
import time

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://hoopshype.com/salaries/players/")

players_links = driver.find_elements(By.XPATH, "//td[@class='name']/a")
links = []

for player_link in players_links:
    links.append(player_link.get_attribute('href'))

for link in links:
    time.sleep(5)
    driver.get(link)
    player = {}
    try:
        player_fullname = driver.find_element(By.XPATH, '//div[@class="player-fullname"]').text
        player['fullname'] = player_fullname
    except:
        player_fullname['fullname'] = ''
    try:
        player_team = driver.find_element(By.XPATH, '//div[@class="player-team"]').text
        player['team'] = player_team
    except:
        player_team['team'] = ''
    try:
        rows = driver.find_elements(By.XPATH, "//span[@class='player-bio-text-line-value']")
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
    
    json_player = json.dumps(player)
    print(json_player)
    time.sleep(2)

    with open('nba_players.json', 'a') as json_file:
        json_file.write(json_player)
        json_file.write(',\n')

driver.quit()

