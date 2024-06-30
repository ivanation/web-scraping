# Librerias a instalar
# pip install lxml
# pip install requests
# pip install beautifulsoup4
from bs4 import BeautifulSoup
import requests
from lxml import html

# URL SEMILLA
url = 'https://www.wikipedia.org/'

# USER AGENT PARA PROTEGERNOS DE BANEOS
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}

# REQUERIMIENTO AL SERVIDOR
response = requests.get(url, headers=headers)
response.encoding = 'utf-8' # Codificar correctamente caracteres extranos

# PARSEO DEL ARBOL HTML
soup = BeautifulSoup(response.text, 'lxml')

# OBTENGO IDIOMAS
items = soup.find_all('div', class_='central-featured-lang')

# PREPARAMOS ARCHIVO PARA GUARDAR
passFile = open('resultados.txt', 'w', encoding="utf-8")

# IMPRIMO
count = 1
for i in items:
    itemLanguage = i.find('strong').text
    linea = f'{count} Idioma: {itemLanguage}\n'
    print(linea)
    # LINEA PARA GUARDAR EN ARCHIVO
    passFile.write(linea)
    count = count + 1

passFile.close()

# PARSEO DEL ARBOL HTML QUE RECIBO COMO RESPUESTA CON LXML
parser = html.fromstring(response.content) # Uso .content para poder codificar los caracteres raros

# OBTENGO IDIOMAS
idiomas = parser.xpath('//div[contains(@class, "central-featured-lang")]//strong/text()')
print(idiomas)


