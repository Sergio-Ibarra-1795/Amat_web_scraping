##Ejemplos de conexión con un sitio web 
## Importamos la biblioteca urllib 
from urllib.request import urlopen

try:
    html = urlopen('https://gozdeveloper.com/gozchenko_maciasnetsov/')
    print(html.read())
except:
    print('No se puede abrir')


print('Aca seguimos')