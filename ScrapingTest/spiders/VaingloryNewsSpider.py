import scrapy


import json
import scrapy

class VaingloryNewsSpider(scrapy.Spider):
    name = 'vainglory'
    start_urls = ['https://www.vainglorygame.com/news/']

    def __init__(self, *args, **kwargs):
        super(VaingloryNewsSpider, self).__init__(*args, **kwargs)
        self.articles = []

    def parse(self, response):
        for element in response.css('.js-news-carousel .slide'):
            title = element.css('h1.white::text').get()
            link = element.css('a.button-big::attr(href)').get()
            image_url = element.css('.bg-image::attr(style)').get()

            if image_url:
                image_url = image_url.split('url(')[-1].split(')')[0]

            self.articles.append({'title': title, 'link': link, 'image_url': image_url})

        self.save_to_json(self.articles)

        yield {'articlesnya adalah': self.articles}

    def save_to_json(self, data):
        try:
            with open('articles.json', 'w') as f:
                json.dump(data, f, indent=4)
            self.log("Data berhasil disimpan ke articles.json")
        except Exception as e:
            self.log(f"Error menyimpan data ke file JSON: {e}")

