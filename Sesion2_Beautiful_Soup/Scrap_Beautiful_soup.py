##Obtener código de una página web y presentarlo en pantalla con formato

## Importamos la biblioteca urllib 
from urllib.request import urlopen

##Importamos beautifulsoup 
from bs4 import BeautifulSoup

try:
    html = urlopen('https://gozdeveloper.com/gozchenko_maciasnetsov/')
    bs = BeautifulSoup(html.read(), 'html.parser')
    print(bs.prettify())
except:
    print('No se puede abrir')


print('Aca seguimos')

