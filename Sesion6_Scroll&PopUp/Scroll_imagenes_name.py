from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import urllib.request
import time



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://infinite-scroll.com/demo/masonry/")
time.sleep(6)
# Set sleep time for the page to load on scroll
scroll_pause_time = 2

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
print(f"Window height: {last_height}")

# If you want to limit the number of scroll loads, add a limit here
scroll_limit = 2

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



images = driver.find_elements(By.XPATH, "//img[@class='image-grid__image']")
images_num = len(images)
print(images_num)

for image in images:
    image_url = image.get_attribute('src')
    print(f"Descargando {image_url}")
    urllib.request.urlretrieve(image_url, Rf"C:/Users/llell/Documents/SIR_Personal/Other_Courses/galery/{image_url.rsplit('/', 1)[1]}")
    print('Imagen descargada!')
    time.sleep(5)    

time.sleep(2) 