from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import urllib.request
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
query = input('¿De qué tema necesitas imágenes? ')
target_folder = os.path.join('./images','_'.join(query.lower().split(' ')))
if not os.path.exists(target_folder):
    os.makedirs(target_folder)

search_url = f"https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={query}&oq={query}&gs_l=img"
driver.get(search_url)
time.sleep(6)

def count_images(driver):
    previous_images = driver.find_elements(By.XPATH, "//div[@jsname='r5xl4']/div")
    print(f"Se encontraron {len(previous_images)} posibles imágenes sin realizar scroll")
    scroll_pause_time = 5
    last_height = driver.execute_script("return document.body.scrollHeight")
    print(f"Moviendo pantalla {last_height} pixeles")
    scroll_limit = 6
    count = 0
    while True and count < scroll_limit:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)
        previous_images = driver.find_elements(By.XPATH, "//div[@jsname='r5xl4']/div")
        print(f"Se encontraron {len(previous_images)} posibles imágenes")    
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        print(f"Nueva posición: {new_height} pixeles")
        if new_height == last_height:
            break
        last_height = new_height
        count += 1


def click_more_button_exists():
    try:
        more_images = driver.find_element(By.XPATH, "//input[@value='Show more results']")
        more_images.click()
        time.sleep(5)
    except:
        print('No hay botón de más')    


def get_images(driver, images_num):
    images = driver.find_elements(By.XPATH, "//div[@jsname='r5xl4']/div")
    time.sleep(6)
    images_saved = 0
    for index, image in enumerate(images):
        try:
            if (index + 1) % 25 != 0:
                new_image = image.find_element(By.XPATH, ".//a/div/img")
                new_image.click()
                time.sleep(3)
                big_image = driver.find_elements(By.XPATH, "//div[@class='v4dQwb']")
                big_image_url = big_image[1].find_element(By.XPATH, ".//a/img")
                big_image_url_complete = big_image_url.get_attribute('src')        
                try:
                    urllib.request.urlretrieve(big_image_url_complete, f"{target_folder}/{index + 1}.jpg")
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





count_images(driver)
click_more_button_exists()
images_num = int(input('Escribe la cantidad de imágenes que necesitas: '))
get_images(driver, images_num)
driver.quit()


