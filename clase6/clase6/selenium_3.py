import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# For headless browser
#chrome_options = Options()
#chrome_options.add_argument("--headless")

print(selenium.__version__)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# For headless browser
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get("https://duckduckgo.com")
search_input = driver.find_element(by=By.XPATH, value="(//input[contains(@class, 'js-search-input')])[1]")
#search_input = driver.find_element_by_xpath("(//input[contains(@class, 'js-search-input')])[1]")
search_input.send_keys("dog")

# Clicks in website
#search_btn = driver.find_element_by_id("search_button_homepage")
#search_btn.click()

# Press Keys in website
search_input.send_keys(Keys.ENTER)

#print(driver.page_source)

time.sleep(15)

driver.close()



#driver.findElement(By.className("className"));
#driver.findElement(By.cssSelector(".className"));
#driver.findElement(By.id("elementId"));
#driver.findElement(By.linkText("linkText"));
#driver.findElement(By.name("elementName"));
#driver.findElement(By.partialLinkText("partialText"));
#driver.findElement(By.tagName("elementTagName"));
#driver.findElement(By.xpath("xPath"));

#driver.findElements(By.className("className"));
#driver.findElements(By.cssSelector(".className"));
#driver.findElements(By.id("elementId"));
#driver.findElements(By.linkText("linkText"));
#driver.findElements(By.name("elementName"));
#driver.findElements(By.partialLinkText("partialText"));
#driver.findElements(By.tagName("elementTagName"));
#driver.findElements(By.xpath("xPath"));