from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader


# DEFINICION DEL ITEM
class Noticia(Item):
    id = Field()
    titular = Field()
    descripcion = Field()


# DEFINIMOS EL SPIDER
class ElUniversoSpider(Spider):
    name = "MiSegundoSpider"
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        # 'FEED_EXPORT_FIELDS': ['id', 'descripcion', 'titular'], # Como ordenar las columnas en el CSV?
        # 'CONCURRENT_REQUESTS': 1 # numero de requerimientos concurrentes 
        #'FEED_EXPORT_ENCODING': 'utf-8'
        'FEED_FORMAT': 'json',
        'FEED_URI': 'datos_de_salida.json'
    }
    start_urls = ['https://www.eluniverso.com/deportes']

    def parse(self, response):
        sel = Selector(response)
        noticias = sel.xpath('//div[contains(@class, "content-feed")]/ul/li')
        for i, elem in enumerate(noticias):
            item = ItemLoader(Noticia(), elem) # Cargo item

            # Llenando mi item a traves de expresiones XPATH
            item.add_xpath('titular', './/h2/a/text()')
            item.add_xpath('descripcion', './/p/text()')
            item.add_value('id', i)
            yield item.load_item() # Retorno mi item lleno


# EJECUCION
# scrapy runspider 5_eluniverso.py -o resultados.csv

# CORRIENDO SCRAPY SIN LA TERMINAL
# process = CrawlerProcess({
#     'FEED_FORMAT': 'json',
#     'FEED_URI': 'datos_de_salida.json'
# })
# process.crawl(ElUniversoSpider)
# process.start()