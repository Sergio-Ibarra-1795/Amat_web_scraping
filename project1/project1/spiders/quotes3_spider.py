import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes3"
    start_urls = [
        'https://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)



# Following links
# <ul class="pager">
#     <li class="next">
#         <a href="/page/2/">Next <span aria-hidden="true">&rarr;</span></a>
#     </li>
# </ul>

# response.css('li.next a').get()
# '<a href="/page/2/">Next <span aria-hidden="true">→</span></a>'

# response.css('li.next a::attr(href)').get()
# '/page/2/'

# response.css('li.next a').attrib['href']
# '/page/2/'






