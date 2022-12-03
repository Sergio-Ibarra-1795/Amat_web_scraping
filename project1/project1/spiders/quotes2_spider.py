import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes2"
    start_urls = [
        'https://quotes.toscrape.com/page/1/',
        'https://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }



# Storing the scraped data
# The simplest way to store the scraped data is by using Feed exports, 
# with the following command:

# scrapy crawl quotes2 -O quotes2.json

# The -O command-line switch overwrites any existing file; 
# use -o instead to append new content to any existing file 
# However, appending to a JSON file makes the file contents 
# invalid JSON. When appending to a file, consider using a 
# different serialization format, such as JSON Lines:

# scrapy crawl quotes2 -o quotes2.jsonl




