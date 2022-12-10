import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'art'
    start_urls = [
        'https://gozdeveloper.com/website2/',
    ]

    def parse(self, response):
        contents = response.xpath("//div[@id='content']/descendant::*/text()").getall()
        all_content = ""
        for content in contents:
            all_content = all_content + " " + content.replace('\n','').lstrip().rstrip() 
        yield {
            'title': response.xpath('//section/h1/text()').get(),
            'content': all_content,
        }

        next_page = response.xpath("//div[@class='links']/a/@href").get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)