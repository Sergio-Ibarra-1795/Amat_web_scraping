from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time
import json


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.eloratings.net")
time.sleep(6)

rows = driver.find_elements(By.XPATH, "//div[@class='grid-canvas']/div")

for row in rows:
    time.sleep(5)
    team_dict = {}
    team_dict['rank'] = row.find_element(By.XPATH, "./div[1]").text
    team_dict['team'] = row.find_element(By.XPATH, "./div[2]").text
    team_dict['rating'] = row.find_element(By.XPATH, "./div[3]").text
    team_dict['avg_rank'] = row.find_element(By.XPATH, "./div[4]").text
    team_dict['avg_rating'] = row.find_element(By.XPATH, "./div[5]").text
    team_dict['one_year_change_rank'] = row.find_element(By.XPATH, "./div[6]").text
    team_dict['one_year_change_rating'] = row.find_element(By.XPATH, "./div[7]").text
    team_dict['total'] = row.find_element(By.XPATH, "./div[8]").text
    team_dict['home'] = row.find_element(By.XPATH, "./div[9]").text
    team_dict['away'] = row.find_element(By.XPATH, "./div[10]").text
    team_dict['neutral'] = row.find_element(By.XPATH, "./div[11]").text
    team_dict['wins'] = row.find_element(By.XPATH, "./div[12]").text
    team_dict['losses'] = row.find_element(By.XPATH, "./div[13]").text
    team_dict['draws'] = row.find_element(By.XPATH, "./div[14]").text
    team_dict['goals_for'] = row.find_element(By.XPATH, "./div[15]").text
    team_dict['goals_against'] = row.find_element(By.XPATH, "./div[16]").text


    print(team_dict['team'])
    print("********************+")

    json_teams = json.dumps(team_dict)
    print(json_teams)

    with open(f'teams.json', 'a') as json_file:
        json_file.write(json_teams)
        json_file.write(',\n')


   
driver.close()


