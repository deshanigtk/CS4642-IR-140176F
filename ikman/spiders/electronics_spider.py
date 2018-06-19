import scrapy
import json


class ElectronicsSpider(scrapy.Spider):
    name = "electronics"
    base_url = 'https://ikman.lk/en/ads/sri-lanka/electronics'
    start_urls = [
        base_url,
    ]

    for i in range(2, 40):
        start_urls.append(base_url + "?page=" + str(i))

    def parse(self, response):
        for href in response.css('div.ui-item div.item-content a::attr(href)'):
            yield response.follow(href, self.parse_article)

    def parse_article(self, response):
        title = response.xpath('/html/body/div[3]/div/div[2]/div/div[1]/div[1]/h1/text()').extract_first()
        location = response.xpath('/html/body/div[3]/div/div[2]/div/div[1]/div[1]/p/span[3]/text()').extract_first()
        posted_by = response.xpath('/html/body/div[3]/div/div[2]/div/div[1]/div[1]/p/span[1]/text()').extract_first()
        posted_time = response.xpath('/html/body/div[3]/div/div[2]/div/div[1]/div[1]/p/span[2]/text()').extract_first()
        price = response.xpath(
            '/html/body/div[3]/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[1]/div/div/span[3]/text()').extract_first()
        condition = response.xpath(
            '/html/body/div[3]/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[1]/dl[1]/dd/text()').extract_first()
        brand = response.xpath(
            '/html/body/div[3]/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[1]/dl[2]/dd/text()').extract_first()
        model = response.xpath(
            '/html/body/div[3]/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[1]/dl[3]/dd/text()').extract_first()
        edition = response.xpath(
            '/html/body/div[3]/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[1]/dl[4]/dd/text()').extract_first()
        authenticity = response.xpath(
            '/html/body/div[3]/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[1]/dl[5]/dd/text()').extract_first()
        features = response.xpath(
            '/html/body/div[3]/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[1]/dl[6]/dd/text()').extract_first()
        description = response.xpath(
            '/html/body/div[3]/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/div[2]/p/text()').extract_first()

        file_name = response.url.split("/")[-1]

        with open("data/" + file_name + ".json", "w+") as outfile:
            json.dump({'title': title,
                       'location': location,
                       'posted_by': posted_by,
                       'posted_time': posted_time,
                       'price': price,
                       'condition': condition,
                       'brand': brand,
                       'model': model,
                       'edition': edition,
                       'authenticity': authenticity,
                       'features': features,
                       'description': description}, outfile, indent=2,
                      sort_keys=True)

            yield {
                'title': title,
                'location': location,
                'posted_by': posted_by,
                'posted_time': posted_time,
                'price': price,
                'condition': condition,
                'brand': brand,
                'model': model,
                'edition': edition,
                'authenticity': authenticity,
                'features': features,
                'description': description
            }
