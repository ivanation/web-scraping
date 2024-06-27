# PIP INSTALL SCRAPY
from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader

# ITEM PARA DATOS
class Pagina(Item):
    titulo = Field()
    url = Field()
    descripcion = Field()


# SPIDER
class ExampleSpider(Spider):
    name = "mercadoLibre"
    allowed_domains = ["mercadolibre.com.ve"]
    start_urls = ["https://www.mercadolibre.com.ve/"]

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        # DATOS PARA GUARDAR EL ARCHIVO
        'FEEDS' : {
            'resultados.json': {
                'format': 'json',
                'encoding': 'utf8',
                'store_empty': False,
                'fields': None,
                'indent': 4,
            }
        }
    }

    def parse(self, response):
        # Selectores: Clase de scrapy para extraer datos
        sel = Selector(response)

        # Extraer el título de la página
        titulo_pagina = sel.xpath('//title/text()').get()

        # Extraer la descripción de la página
        descripcion_pagina = sel.xpath('//meta[@name="description"]/@content').get()

        # Extraer la URL de la página
        url_pagina = response.url

        # Crear un objeto Item
        item = Pagina(titulo=titulo_pagina, url=url_pagina, descripcion=descripcion_pagina)

        # Imprimir el título y la URL
        print(f"Título: {titulo_pagina}")
        print(f"URL: {url_pagina}")
        print(f"descripcion_pagina: {descripcion_pagina}")

        # Guardar el objeto Item en el archivo JSON
        yield item