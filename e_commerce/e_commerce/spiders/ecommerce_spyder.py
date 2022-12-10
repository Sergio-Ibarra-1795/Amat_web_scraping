import scrapy 

class EcommerceSpider (scrapy.Spider):
    name ='productos'
    allowed_domains = []
    start_urls = ['https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page=1']


    def parse (self,response):
        ##Lo primero que queremos hacer es llegar a la primer pantalla
        ## Despues se obtienen solo los productos (para cada uno de los elementos en la lista productos, extrae el enlace)
        products = response.xpat('//h4/a')
        ## (para cada uno de los elementos en la lista productos, extrae el enlace)
        ##SE VA A EJECXUTAR 6 VECES Y DESPUES VA A IR AL  BOTON NEXT_PAGE
        for product in products:
            #Se obtiene el link de cada producto
            link = product.xpath('/@href').get()
            ##Una vez que abras en enlace de link, parsea lo que esté adentro 
            yield response.follow(url=link, callback=self.parse_product)
        next_page = response.xpath("(//a[@rel='next']'])/@href'").get()
        if next_page:
            yield response.follow(url="https://webscraper.io" + next_page, callback=self.parse)


##Ya estamos dentro del enlace de cada prodcuto y vamos a parsear esa pagina y obtener los datos que nos ineresan
    def parse_product (self, response):
    ##response.xpath()  ya contiene el enlace de cada producto, el que nos lleva a la página individual de cada producto 
        price = response.xpath('//h4[1]/text').get()
        name = response.xpath('//h4[2]/text').get()
        description = response.xpath("//p[@class = 'description']/text()")
        yield{
            'name': name,
            'price': price,
            'description': description
        }


    
        