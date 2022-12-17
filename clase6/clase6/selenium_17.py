from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time
import json


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://scrollmagic.io/examples/advanced/infinite_scrolling.html")
time.sleep(6)
# Set sleep time for the page to load on scroll
scroll_pause_time = 2

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
print(f"Window height: {last_height}")

# If you want to limit the number of scroll loads, add a limit here
scroll_limit = 57

count = 0
while True and count < scroll_limit:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(scroll_pause_time)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    print(f"New height: {new_height}")
    if new_height == last_height:
        break
    last_height = new_height
    count += 1

time.sleep(2) 

rows = driver.find_elements(By.XPATH, "//div[@class='box1']")
rows_num = len(rows)
print(rows_num)





