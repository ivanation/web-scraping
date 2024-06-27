# Librerias a instalar
# pip install lxml
# pip install requests
# pip install beautifulsoup4
from bs4 import BeautifulSoup
import requests

# URL SEMILLA
url = 'https://scrapingclub.com/exercise/list_basic/?page=1'

# USER AGENT PARA PROTEGERNOS DE BANEOS
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}

# REQUERIMIENTO AL SERVIDOR
response = requests.get(url, headers=headers)
response.encoding = 'utf-8' # Codificar correctamente caracteres extranos

# PARSEO DEL ARBOL HTML
soup = BeautifulSoup(response.text, 'lxml')

# OBTENGO PRODUCTOS PRIMERA PAGINA
items = soup.find_all('div', class_='w-full rounded border')
count = 1

# IMPRIMO
count = 1

for i in items:
    itemName = i.find('h4').text.strip('\n')
    itemPrice = i.find('h5').text
    print(f'{count} Name: {itemName} Price: {itemPrice}')
    count = count + 1

# OBTENGO LINKS DE PAGINAS
pages = soup.find('nav', class_='pagination')
urls = []
links = pages.find_all('a')

# LLENO ARRAY CON LINKS
for link in links:
    # si el valor es diferente a 1,2,3,4 es null por ejemplo next o last
    pageNum = int(link.text) if link.text.isdigit() else None
    if pageNum != None:
        x = link.get('href')
        urls.append(x)

#print(urls)

# IMPRIMO PARA CADA LINK
for i in urls:
    newUrl = 'https://scrapingclub.com' + i
    response = requests.get(newUrl)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='w-full rounded border')

    for i in items:
        itemName = i.find('h4').text.strip('\n')
        itemPrice = i.find('h5').text
        print(f'{count} Name: {itemName} Price: {itemPrice}')
        count = count + 1