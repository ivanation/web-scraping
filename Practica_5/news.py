# PIP INSTALL SCRAPY
from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

# ITEM PARA DATOS
class Pagina(Item):
    titulo = Field()
    url = Field()
    descripcion = Field()
    date = Field()
    text = Field()


# SPIDER
class ExampleSpider(CrawlSpider):
    name = "apnews"
    
    # Url semilla a la cual se hara el primer requerimiento
    start_urls = ["https://apnews.com/article/trump-biden-debate-age-democrats-b93d7ffaad75fd423ea3953fe16287f0"]

    custom_settings = {
        'CLOSESPIDER_PAGECOUNT': 10, # terminar en 10 peticiones
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        # DATOS PARA GUARDAR EL ARCHIVO
        'FEEDS' : {
            'resultados.json': {
                'format': 'json',
                'encoding': 'utf8',
                'store_empty': False,
                'fields': None,
                'indent': 4
            }
        },
    }

    # Tiempo de espera entre cada requerimiento. Nos ayuda a proteger nuestra IP.
    download_delay = 2

    # Reduce el espectro de busqueda de URLs. No nos podemos salir de los dominios de esta lista
    allowed_domains = ["apnews.com"]

    # Reglas para direccionar el movimiento de nuestro Crawler a traves de las paginas
    rules = [Rule(LinkExtractor(allow=r"article/(.*)"), callback='parse_item', follow=True)]

    def parse_item(self, response):
        
        # Selectores: Clase de scrapy para extraer datos
        sel = Selector(response)

        # Extraer el título de la página
        titulo_pagina = sel.xpath('//title/text()').get()

        # Extraer la descripción de la pagina
        descripcion_pagina = sel.xpath('//meta[@name="description"]/@content').get()

        # Extraer la URL de la página
        url_pagina = response.url

        # Extraer la fecha de la noticia
        date_pagina = sel.xpath('//meta[@property="article:published_time"]/@content').get()

        # Extraer la texto de la noticia
        texto_pagina = sel.xpath('//div[@class="RichTextStoryBody RichTextBody"]/p/text()').getall()

        # Crear un objeto Item
        item = Pagina(titulo=titulo_pagina, url=url_pagina, descripcion=descripcion_pagina, date=date_pagina, text=texto_pagina)

        # Imprimir el título y la URL
        print(f"Título: {titulo_pagina}")
        print(f"URL: {url_pagina}")
        print(f"descripcion_pagina: {descripcion_pagina}")
        print(f"fecha_pagina: {date_pagina}")
        print(f"texto: {texto_pagina}")

        # Guardar el objeto Item en el archivo JSON
        yield item