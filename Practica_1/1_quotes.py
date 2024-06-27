# Librerias a instalar
# pip install lxml
# pip install requests
# pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup

# URL SEMILLA
url = 'https://quotes.toscrape.com/'

# USER AGENT PARA PROTEGERNOS DE BANEOS
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}

# REQUERIMIENTO AL SERVIDOR
response = requests.get(url, headers=headers)
response.encoding = 'utf-8' # Codificar correctamente caracteres extranos

# PARSEO DEL ARBOL HTML
soup = BeautifulSoup(response.text, 'lxml')

# OBTENGO QUOTES
quotes = soup.find_all('span', class_='text')

# OBTENGO AUTORES
authors = soup.find_all('small', class_='author')

# OBTENGO TAGS
tags = soup.find_all('div', class_='tags')

# IMPRIMO
for i in range(0, len(quotes)) :
    print(quotes[i].text)
    print(authors[i].text)
    # MEJOR FORMATO DE TAGS
    quoteTags = tags[i].find_all('a', class_='tag')
    for quoteTag in quoteTags:
        print(quoteTag.text)
