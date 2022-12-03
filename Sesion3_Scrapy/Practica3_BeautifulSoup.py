# sCRAPING DE UNA PÁGINA CON MULTIPLES PÁGINAS CON N número de páginas definidas 

# Importamos las bibliotecas urllib y bs4
import requests
from bs4 import BeautifulSoup

main_url = 'http://books.toscrape.com/catalogue/'
##books_file = R'C:\Users\sergi\OneDrive\Documentos\SIR_personal\AMAT_Python_scrapping\Practica3\books.csv'
books_file = R'C:\Users\Sergio\Documents\SIR_Personal_Dell\AMAT_Python_scrapping\Practica3\books.csv'
##images_directory = R'C:\Users\sergi\OneDrive\Documentos\SIR_personal\AMAT_Python_scrapping\Practica3\images'
images_directory = R'C:\Users\Sergio\Documents\SIR_Personal_Dell\AMAT_Python_scrapping\Practica3\images'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
pages_to_scrape = 50


def get_all_info_from_page(url):
    # Se hace la sopa
    # Primero se hace request, que es el acto de hacer click en el navegador y llegar a la ruta
    html = requests.get(url, headers=headers)
    # Se debe embellecer el contenido de obtenido de la página (ESTE YA ES EL OBJETO DE OBJETOS CON TODAS LAS ETIQUETAS)
    bs = BeautifulSoup(html.content, 'html.parser')
    # Ahora necesita entrar a la @pagina de cada libro
    links = bs.find_all("img", class_="thumbnail")


    for link in links:
        print(link.parent['href'])
        # Se genera ahora una sopa de cada link
        html = requests.get(main_url + link.parent['href'], headers=headers)
        bs = BeautifulSoup(html.content, 'html.parser')

        # Dentro de cada página del libro encuentra el titulo, precio, etc
        title = bs.find('h1').text
        price = bs.find("p", class_="price_color").text
        stock = bs.find("p", class_="availability").text.replace('\n','').lstrip()
        try:
            description = bs.find("div", id="product_description").next_sibling.next_sibling.text
        except:
            description = "no tiene"    
        upc = bs.table.tr.td.text
        product_type = bs.table.tr.next_sibling.next_sibling.td.text

        with open(books_file, 'a') as file_object:
            file_object.write(f"{title} | {price} | {stock} | {description} | {upc} | {product_type}\n")

# Ahora para scrapear las n número de páginas 
page_numbers = range(1, pages_to_scrape + 1)
for page_number in page_numbers:
    print(str(page_number))
    get_all_info_from_page(main_url + 'page-' + str(page_number) + '.html')

