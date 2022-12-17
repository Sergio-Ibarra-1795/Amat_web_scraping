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

#select_1 = Select(driver.find_element(By.XPATH, "//select[@id='idPeriodoMensual']"))
#select_1.select_by_visible_text("Octubre 2022")
#time.sleep(3)

#select_2 = Select(driver.find_element(By.XPATH, "//select[@id='idOperadora']"))
#select_2.select_by_visible_text("SAM - 70016")
#time.sleep(3)

button = driver.find_element(By.XPATH, "//button[@class='btn btn-default']")
button.click()

time.sleep(5)

link = driver.find_element(By.XPATH, "//li[@class='page-next']/a")
link.click()

time.sleep(3)

driver.quit()
