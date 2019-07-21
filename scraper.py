import scrapy


class PageSpider(scrapy.Spider):
    name = "page"
    start_urls = ['https://<PUBLIC_URL>']

    def parse(self, response):
        for article_url in response.css('.title a ::attr("href")').extract():
            yield response.follow(article_url, callback=self.parse_article)

    def parse_article(self, response):
        title = response.xpath(".//h3[@class='icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title']/descendant::text()").extract()
        description = response.xpath(".//div[@class='jobsearch-jobDescriptionText']/descendant::text()").extract()
        yield {'title': ''.join(title) ,'description': ''.join(description)}

