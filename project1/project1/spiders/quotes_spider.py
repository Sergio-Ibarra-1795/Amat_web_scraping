import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://quotes.toscrape.com/page/1/',
            'https://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')


# name: 
# identifies the Spider. It must be unique within a project, 
# that is, you can’t set the same name for different Spiders.

# start_requests: 
# must return an iterable of Requests (you can 
# return a list of requests or write a generator function) which 
# the Spider will begin to crawl from. Subsequent requests 
# will be generated successively from these initial requests.

# parse:
# a method that will be called to handle the response 
# downloaded for each of the requests made. The response 
# parameter is an instance of TextResponse that holds 
# the page content and has further helpful methods to handle it.

# The parse() method usually parses the response, extracting
# the scraped data as dicts and also finding new URLs to
# follow and creating new requests (Request) from them.

# How to run the spider?
# go to top level directory and
# scrapy crawl quotes


# We can also use this code
#import scrapy

#class QuotesSpider(scrapy.Spider):
#    name = "quotes"
#    start_urls = [
#        'https://quotes.toscrape.com/page/1/',
#        'https://quotes.toscrape.com/page/2/',
#    ]

#    def parse(self, response):
#        page = response.url.split("/")[-2]
#        filename = f'quotes-{page}.html'
#        with open(filename, 'wb') as f:
#            f.write(response.body)

# The best way to learn how to extract data with scrapy is trying
# selectors using the scrapy shell
# scrapy shell 'https://quotes.toscrape.com/page/1/'
