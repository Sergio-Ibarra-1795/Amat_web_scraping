# Scraper de Yahoo Finance
# Autor: Goz
# Descripción: Obtener información de una página utilizando bs4
        
# Importamos las bibliotecas urllib y bs4
import requests
from bs4 import BeautifulSoup
import time

main_url = 'https://finance.yahoo.com/most-active?offset=0&count=200'
pages_url = 'https://finance.yahoo.com/'
books_file = R'\Users\sergi\OneDrive\Documentos\SIR_personal\AMAT_Python_scrapping\Practica2\stocks.csv'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}


def get_stock_information(url):
    html = requests.get(url, headers=headers)
    bs = BeautifulSoup(html.content, 'html.parser')
    name = bs.find("h1", class_="D(ib) Fz(18px)").text
    previous_close = bs.find(attrs={"data-test": "PREV_CLOSE-value"}).text
    open_value = bs.find(attrs={"data-test": "OPEN-value"}).text
    bid_value = bs.find(attrs={"data-test": "BID-value"}).text
    ask_value = bs.find(attrs={"data-test": "ASK-value"}).text
    days_range_value = bs.find(attrs={"data-test": "DAYS_RANGE-value"}).text
    week_range_value = bs.find(attrs={"data-test": "FIFTY_TWO_WK_RANGE-value"}).text
    volume_value = bs.find(attrs={"data-test": "TD_VOLUME-value"}).text
    average_volume = bs.find(attrs={"data-test": "AVERAGE_VOLUME_3MONTH-value"}).text
    previous_close = bs.find(attrs={"data-test": "PREV_CLOSE-value"}).text
    market_cap_value = bs.find(attrs={"data-test": "MARKET_CAP-value"}).text

    with open(books_file, 'a') as file_object:
        file_object.write(f"{name} | {previous_close} | {open_value} | {bid_value} | {ask_value} | {days_range_value} | {week_range_value} | {volume_value} | {average_volume} | {previous_close} | {market_cap_value}\n")


html = requests.get(main_url, headers=headers)
bs = BeautifulSoup(html.content, 'html.parser')
links = bs.find_all("a", class_="Fw(600) C($linkColor)")
for link in links:
    print(pages_url + link['href'])
    get_stock_information(pages_url + link['href'])
    time.sleep(7)            

