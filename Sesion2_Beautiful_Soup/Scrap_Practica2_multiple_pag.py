# Practica No. 2
# Obtener información de un sitio web estático con múltoples páginas

# Importamos la biblioteca urllib y bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup

website = 'https://gozdeveloper.com/website2/'


def get_content(url):
    html = urlopen(url)
    bs = BeautifulSoup(html.read(), 'html.parser')
    title = bs.find('h1').text
    content = bs.find('div', id="content").text
    all_content = '\n' + title + '\n' + content.replace('\n','').lstrip()
    return all_content

html = urlopen(website)    
bs = BeautifulSoup(html.read(), 'html.parser')

links = bs.find_all('li')
website_content = []
for link in links:
    website_content.append(get_content(website + link.a['href']))


with open(R'C:\Users\sergi\OneDrive\Documentos\SIR_personal\AMAT_Python_scrapping\Practica2\vincent_vangogh.txt', 'w') as file_object:
    file_object.write('PRACTICA 2 - Taller de Web Scraping\n')
    for content in website_content:
      file_object.write(f"\n{content}")
