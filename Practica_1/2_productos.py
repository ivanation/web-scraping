# Librerias a instalar
# pip install lxml
# pip install requests
# pip install beautifulsoup4
from bs4 import BeautifulSoup
import requests

# URL SEMILLA
url = 'https://scrapingclub.com/exercise/list_basic/?page=2'

# USER AGENT PARA PROTEGERNOS DE BANEOS
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}

# REQUERIMIENTO AL SERVIDOR
response = requests.get(url, headers=headers)
response.encoding = 'utf-8' # Codificar correctamente caracteres extranos

# PARSEO DEL ARBOL HTML
soup = BeautifulSoup(response.text, 'lxml')

# OBTENGO PRODUCTOS
items = soup.find_all('div', class_='w-full rounded border')

# PREPARAMOS ARCHIVO PARA GUARDAR
passFile = open('resultados_2.csv', 'w')

# IMPRIMO
count = 1
for i in items:
    itemName = i.find('h4').text.strip('\n')
    itemPrice = i.find('h5').text
    linea = f'{count} Name: {itemName} Price: {itemPrice}\n'
    print(linea)
    # LINEA PARA GUARDAR EN ARCHIVO
    passFile.write(linea)
    count = count + 1

passFile.close()