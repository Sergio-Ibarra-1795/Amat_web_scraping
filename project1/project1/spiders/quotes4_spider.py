import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes4"
    start_urls = [
        'https://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('span small::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)



# As a shortcut for creating Request objects you can use response.follow:

# Unlike scrapy.Request, response.follow supports relative URLs
# directly - no need to call urljoin.

# You can also pass a selector to response.follow instead of a string; 
# this selector should extract necessary attributes:
#for href in response.css('ul.pager a::attr(href)'):
#    yield response.follow(href, callback=self.parse)

# For <a> elements there is a shortcut: response.follow uses 
# their href attribute automatically. So the code can
# be shortened further:
#for a in response.css('ul.pager a'):
#    yield response.follow(a, callback=self.parse)

# To create multiple requests from an iterable, 
# you can use response.follow_all instead:
#anchors = response.css('ul.pager a')
#yield from response.follow_all(anchors, callback=self.parse)

#or, shortening it further:

#yield from response.follow_all(css='ul.pager a', callback=self.parse)















