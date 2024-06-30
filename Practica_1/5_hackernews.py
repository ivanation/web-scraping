# Librerias a instalar
# pip install lxml
# pip install requests
# pip install beautifulsoup4
from bs4 import BeautifulSoup
import requests
from lxml import html

# URL SEMILLA
url = 'https://news.ycombinator.com/'

# USER AGENT PARA PROTEGERNOS DE BANEOS
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}

# REQUERIMIENTO AL SERVIDOR
response = requests.get(url, headers=headers)
response.encoding = 'utf-8' # Codificar correctamente caracteres extranos

# PARSEO DEL ARBOL HTML
soup = BeautifulSoup(response.text, 'lxml')

# OBTENGO NOTICIAS
noticias = soup.find_all('tr', class_='athing')

# PREPARAMOS ARCHIVO PARA GUARDAR
passFile = open('resultados.csv', 'w', encoding="utf-8")

# IMPRIMO
count = 1 # count comienza en 1
passFile.write('count;news;url;score;\n') # encabezados del csv
for noticia in noticias:
    titulo = noticia.find('span', class_='titleline').text
    url = noticia.find('span', class_='titleline').find('a').get('href')
    
    try:
        temp = noticia.find_next_sibling()
        score_tmp = temp.find('span', class_='score').text
        score_tmp = score_tmp.replace('points', '').strip()
        score = int(score_tmp)
    except Exception as e:
        score = 0
        print(e)
        print('No se encontró score')

    linea = f'{count};{titulo};{url};{score};\n'
    print(linea)
    # LINEA PARA GUARDAR EN ARCHIVO
    passFile.write(linea)
    count = count + 1

passFile.close()

# USANDO LA LIBRERIA LXML
# PARSEO DEL ARBOL HTML QUE RECIBO COMO RESPUESTA CON LXML
parser = html.fromstring(response.content) # Uso .content para poder codificar los caracteres raros

# OBTENGO DATOS
titles = parser.xpath('//span[@class="titleline"]//a/text()')
print(titles)
urls = parser.xpath('//span[@class="titleline"]//a/@href')
print(urls)