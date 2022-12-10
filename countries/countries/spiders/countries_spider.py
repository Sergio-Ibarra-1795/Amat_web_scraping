import scrapy 

class CountriesSpider (scrapy.Spider):
    name ='countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']


    def parse (self,response):
        countries = response.xpath('//td/a')
        for country in countries:
            ##  Contendrpa todos los paises que es el texto que está en el xpath 
            name = country.xpath('.//text()')
            ##link contendrá el href de cada pais
            link = country.xpath ('.//@href')
            ##Vamos a darle click al enlace de cada pais
            yield response.follow(url=link, callback=self.parse_country, meta={'country_name':name})
    
    ##Una vez que se le da click debemos hacer como tal el parseo del country 
    def parse_country (self, response):
        name = response.request.meta['country_name'] 
        rows = response.xpath("(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr")
        for row in rows: 
            year = row.xpath('//td[1]/text()').get()
            population = row.xpath('//td[2]/strong/text()').get()
            migrants = row.xpath('//td[5]/text()').get()
        yield {
            'country_name':name,
            'year': year,
            'population':population,
            'migrants':migrants
        }