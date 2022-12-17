from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://duckduckgo.com")

search_input = driver.find_element(by=By.XPATH, value="//input[@id='search_form_input_homepage']")
search_input.send_keys("Top algoritmos de búsqueda")
search_input.send_keys(Keys.ENTER)

time.sleep(5)

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
