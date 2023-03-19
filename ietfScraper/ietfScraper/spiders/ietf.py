import scrapy


class IetfSpider(scrapy.Spider):
    name = 'ietf'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['https://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):
        title = response.css('span.title::text').get()
        title = response.xpath('//span[@class="title"]/text()').get()
        author = response.xpath('//span[@class="author-name"]/text()').get()
        headings = response.xpath('//span[@class="subheading"]/text()').getall()
        return {"title": title,
                "author name": author,
                "main points": headings}
        
        pass
