# Obtener todas la imágenes de un sitio

# Importamos la biblioteca urllib y bs4
from urllib.request import urlopen
import urllib.request
from bs4 import BeautifulSoup
import re

html = urlopen('https://gozdeveloper.com/demo1/')    
bs = BeautifulSoup(html.read(), 'html.parser')
    
images = bs.find_all('img', {'src':re.compile('[A-Za-z]*.[png|jpg]')})
for image in images:
    image2 = image['src'].replace('img','')
    url = 'https://gozdeveloper.com/demo1/' + image['src']
    print(url)
    urllib.request.urlretrieve(url, fR"C:\Users\sergi\OneDrive\Documentos\SIR_personal\AMAT_Python_scrapping\Practica1\{image2}")

