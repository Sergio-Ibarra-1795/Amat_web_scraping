from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import urllib.request
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
query = "90s movies posters"
search_url = f"https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={query}&oq={query}&gs_l=img"
driver.get(search_url)
time.sleep(6)

previous_images = driver.find_elements(By.XPATH, "//div[@jsname='r5xl4']/div")
print(f"Se encontraron {len(previous_images)} posibles imágenes")

scroll_pause_time = 5
last_height = driver.execute_script("return document.body.scrollHeight")
print(f"Window height: {last_height}")
scroll_limit = 6
count = 0

while True and count < scroll_limit:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
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

try:
    more_images = driver.find_element(By.XPATH, "//input[@value='Show more results']")
    more_images.click()
except:
    print('No hay botón de más')    


time.sleep(5)
images = driver.find_elements(By.XPATH, "//div[@jsname='r5xl4']/div")
time.sleep(6)
images_num = 100
images_saved = 0


for index, image in enumerate(images):
    try:
        if index not in [24, 49, 74, 99, 124, 149, 174]:
            new_image = image.find_element(By.XPATH, ".//a/div/img")
            new_image.click()
            time.sleep(3)

            big_image = driver.find_elements(By.XPATH, "//div[@class='v4dQwb']")
            big_image_url = big_image[1].find_element(By.XPATH, ".//a/img")
            big_image_url_complete = big_image_url.get_attribute('src')        
            try:
                urllib.request.urlretrieve(big_image_url_complete, f"/home/goz/Courses/web_scraping/practica_1/clase3/selenium/movies90/{index}.jpg")
                print('Imagen descargada!')
                images_saved += 1
            except:
                print('No se puede descargar')    
            print(f"Tenemos {images_saved} imagenes")

    except:
        print('No se puede descargar')
    if images_saved == images_num - 1:
        break            
    time.sleep(1)    

time.sleep(2) 
print(f" Se descargaron {images_saved} imágenes de {len(images)} encontradas")


time.sleep(11)


