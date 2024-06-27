# Librerias a instalar
# pip install lxml
# pip install requests
# pip install beautifulsoup4
import requests
import json

# UPC code
upc = "012993441012"

# URL SEMILLA
url = "https://api.upcitemdb.com/prod/trial/lookup"

# DICCIONARIO DE PARAMETROS 
parametros = {
    "upc": upc
}

# USER AGENT PARA PROTEGERNOS DE BANEOS
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}

# REQUERIMIENTO AL SERVIDOR
response = requests.get(url, headers=headers, params=parametros)

# CHECK SI REQUERIMIENTO FUE EXITOSO
if response.status_code == 200:
    
    # EXTRAER JSON
    content = response.content

    # Parseo la respuesta en formato JSON. Requests automaticamente lo convierte en un diccionario de Python
    data = response.json()

    # EXTRAIGO DATOS E IMPRIMO
    item = data['items']
    itemInfo = item[0]
    title = itemInfo['title']
    brand = itemInfo['brand']
    print(title)
    print(brand)

else:
    print("Error:", response.status_code)
