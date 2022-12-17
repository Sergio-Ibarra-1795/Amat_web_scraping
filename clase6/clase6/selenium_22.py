from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import urllib.request
import time



driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
query = "best programmers"
search_url = f"https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={query}&oq={query}&gs_l=img"
driver.get(search_url)
time.sleep(6)

previous_images = driver.find_elements(By.XPATH, "//div[@jsname='r5xl4']/div")
print(f"Se encontraron {len(previous_images)} posibles imágenes")

# Set sleep time for the page to load on scroll
scroll_pause_time = 5
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
print(f"Window height: {last_height}")
# If you want to limit the number of scroll loads, add a limit here
scroll_limit = 6
count = 0
while True and count < scroll_limit:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(scroll_pause_time)
    previous_images = driver.find_elements(By.XPATH, "//div[@jsname='r5xl4']/div")
    print(f"Se encontraron {len(previous_images)} posibles imágenes")    

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    print(f"New height: {new_height}")
    if new_height == last_height:
        break
    last_height = new_height
    count += 1

more_images = driver.find_element(By.XPATH, "//input[@value='Show more results']")
more_images.click()


time.sleep(5)
images = driver.find_elements(By.XPATH, "//div[@jsname='r5xl4']/div")
time.sleep(6)
images_num = 126
images_saved = 0

print(f"Se encontraron {len(images)} posibles imágenes")

for index, image in enumerate(images):
    try:
        new_image = image.find_element(By.XPATH, ".//a/div/img")
        image_url = new_image.get_attribute('src')
        urllib.request.urlretrieve(image_url, f"/home/goz/Courses/web_scraping/practica_1/clase3/selenium/gallery/{index}.jpg")
        print('Imagen descargada!')
        images_saved += 1
        print(f"Tenemos {images_saved} imagenes")
    except:
        print('No se puede descargar')
    if images_saved == images_num - 1:
        break            
    time.sleep(1)    

time.sleep(2) 
print(f" Se descargaron {images_saved} imágenes de {len(images)} encontradas")


time.sleep(11)

