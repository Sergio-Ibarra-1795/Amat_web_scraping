from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import json

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.scrapethissite.com/pages/ajax-javascript/")

links = driver.find_elements(By.XPATH, "//a[@class='year-link']")

all_movies = []

for link in links:
    movie = {}
    year = link.text
    link.click()
    time.sleep(5)

    rows = driver.find_elements(By.XPATH, "//tbody[@id='table-body']/tr")

    for row in rows:
        title = row.find_element(By.XPATH, ".//td[1]").text
        nominations = row.find_element(By.XPATH, ".//td[2]").text
        awards = row.find_element(By.XPATH, ".//td[3]").text

        movie['year'] = year
        movie['title'] = title
        movie['nominations'] = int(nominations)
        movie['awards'] = int(awards)

        json_movie = json.dumps(movie)
        all_movies.append(json_movie)
        print(json_movie)


with open('movies.json', 'a') as json_file:
    json_file.write("[\n")
    for movie in all_movies:
        json_file.write(movie)
        json_file.write(',\n')
    json_file.write("]\n")


driver.quit()
