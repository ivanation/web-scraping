# Librerias a instalar
# pip install lxml
# pip install requests
# pip install beautifulsoup4
from bs4 import BeautifulSoup
import requests
from lxml import html

# URL SEMILLA
url = 'https://stackoverflow.com/questions'

# USER AGENT PARA PROTEGERNOS DE BANEOS
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}

# REQUERIMIENTO AL SERVIDOR
response = requests.get(url, headers=headers)
response.encoding = 'utf-8' # Codificar correctamente caracteres extranos

# PARSEO DEL ARBOL HTML
soup = BeautifulSoup(response.text, 'lxml')

# OBTENGO TITULOS DE PREGUNTAS
preguntas = soup.find_all('h3', class_='s-post-summary--content-title')

# PREPARAMOS ARCHIVO PARA GUARDAR
passFile = open('resultados.csv', 'w', encoding="utf-8")

# IMPRIMO
count = 1
passFile.write('id;pregunta;\n')
for i in preguntas:
    titulo = i.find('a').text
    linea = f'{count};{titulo};\n'
    print(linea)
    # LINEA PARA GUARDAR EN ARCHIVO
    passFile.write(linea)
    count = count + 1

passFile.close()