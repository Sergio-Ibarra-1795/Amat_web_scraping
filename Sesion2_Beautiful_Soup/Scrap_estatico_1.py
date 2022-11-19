##Practica 1
## Obtener información de un sitio web estatico

## Importamos la biblioteca urllib 
from urllib.request import urlopen

##Importamos beautifulsoup 
from bs4 import BeautifulSoup

import inspect

try:
    html = urlopen('https://gozdeveloper.com/gozchenko_maciasnetsov/')
    bs = BeautifulSoup(html.read(), 'html.parser')

    ##Obtenemos e-mail, telefono y universidad 
    contacts = bs.find_all('div', {'class':'contact'})
    email = contacts[0].text
    email = email.lstrip()
    phone = contacts[1].text
    phone = phone.lstrip()
    university = contacts[2].text
    university = university.lstrip()
    print(email,phone, university)

    ##Obtenemos el nombre completo 
    complete_name = bs.find('h1', id='name').string
    print(complete_name)

    ##Obtenemos el trabajo
    job = bs.find('h2', id='job').string
    print(job)

    # Obtenemos la semblanza
    semblance = bs.find('div', id='presentation')
    semblance_list = []
    for child in semblance.children:
        if child != '\n':
            semblance_list.append(inspect.cleandoc(child.text).replace('\n',''))
    
    print(semblance_list)

   ##Obtenemos la frase
    phrase= bs.find('div', id='phrase').string
    print(phrase)


    ##Obtenemos las lineas de investigacion
    research_lines = bs.find('ul', id='research_lines')
    research_lines_list = []
    for child in research_lines.children:
        if child !=  '\n':
           research_lines_list.append(child.text[0:-1])

    print(research_lines_list)

    ##Obtenemos las publicacones destacadas
    publications = bs.find('ul', id='publications')
    publications_list = []
    for child in publications.children:
        if child !=  '\n':
           publications_list.append(child.text.lstrip())

    print(publications_list)

    ##Obtenemos los awards
    awards = bs.find('ul', id='awards')
    awards_list = []
    for child in awards.children:
        if child !=  '\n':
           awards_list.append(child.text)

    print(awards_list)


    ##Obtenemos Educacion y trayectoria 
    grades = bs.find('ul', id='grades')
    grades_list = []
    for child in grades.children:
        if child !=  '\n':
           grades_list.append(child.text)

    print(grades_list)


    with open(R'C:\Users\sergi\OneDrive\Documentos\SIR_personal\AMAT_Python_scrapping\Practica1\gozchenko.txt', 'w') as file_object:

        file_object.write('PRACTICA 1 - Taller de Web Scraping\n')
        file_object.write(f'\nAcademico/a: {complete_name}')
        file_object.write(f'\nEmail: {email}')
        file_object.write(f'\nTélefono: {phone}')
        file_object.write(f'\nUniversidad: {university}')
        file_object.write(f'\n---------------------------------------------------------------')
        for semblance in semblance_list:
            file_object.write(f'\n{semblance}')
        file_object.write(f'\n---------------------------------------------------------------')
        file_object.write(f'\nLíneas de investigación:')
        for research_line in research_lines_list:
            file_object.write(f'\n{research_line}')
        file_object.write(f'\n---------------------------------------------------------------')
        file_object.write(f'\nPublicaciones:')        
        for publication in publications_list:
            file_object.write(f'\n{publication}')                
        file_object.write(f'\n---------------------------------------------------------------')
        file_object.write(f'\nPremios:')        
        for award in awards_list:
            file_object.write(f'\n{award}')


except:
    print('No se puede abrir')

