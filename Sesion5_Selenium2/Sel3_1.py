import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")

search_input = driver.find_element(by=By.XPATH, value="//input[@class='gLFyf']")
search_input.send_keys("Qatar 2022 ganador")
time.sleep(2)
search_input.send_keys(Keys.ENTER)
time.sleep(5)

driver.quit()
